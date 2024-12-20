from bs4 import BeautifulSoup, Tag, ResultSet
from readability import Document
from selenium.common.exceptions import WebDriverException

from src.nlp import classifier, keywords_extractor, pos_phrase
from src.verification.website_driver import create_driver
from src.verification.parse_helper import filter_title, filter_description
from src.verification.types import UrlContext, ValidationResult, PassageContext

import requests
import logging

logger = logging.getLogger('HyperlinkVerifier')

foo = 'foo'


class HyperlinkVerifier:

    # ------------ constructor ------------------ #
    def __init__(self):
        logger.info('__init__()')
        self.webdriver = create_driver()
        self.curr_soup: (BeautifulSoup | None) = None
        self.curr_doc: (Document | None) = None
        self.curr_url: UrlContext = {}
        return

    # ------------ browser config ------------------ #

    # ------------ read url ------------------ #

    def read_url(self, url: str):
        logger.info('read_url() %s', url)

        # clean up previous url data
        self.curr_url.clear()
        self.curr_doc = None
        self.curr_soup = None

        self.curr_url['check_code'] = self._check_url(url)
        if (self.curr_url['check_code'] > 3):
            return self.curr_url['check_code']

        retry_limit = 2
        number_try = 0
        while number_try < retry_limit:
            try:
                # open url
                self.webdriver.get(url)
                # read the source page
                html = self.webdriver.page_source
                # parse html into string
                soup = BeautifulSoup(html, "lxml")
                self.curr_soup = soup
                if (self.curr_soup and self._soup_examine()):
                    return 0
                else:
                    return 1 if self.curr_url['check_code'] == 0 else self.curr_url['check_code']
            except WebDriverException as e:
                logger.warning(e)
                number_try += 1

        return 1 if self.curr_url['check_code'] == 0 else self.curr_url['check_code']

    def _soup_examine(self):
        """
        Validate if the soup from current page
        """
        title = self._get_title()
        summary = self._get_summary()
        body = self._get_cleaned_body()

        logger.info('_soup_examine() %s', {
                    'title': title, 'summary': summary, 'body_len': len(body)})

        # Refactor - how to address cloudFlare detection
        isCaptcha = ('captcha' in summary) and body == foo
        isSoupEmpty = summary == foo and body == foo
        if (isCaptcha or isSoupEmpty):
            # encounter recaptcha bot page - return 0
            return False

        return True

    def _check_url(self, url: str):
        """
        Check if a url is valid:
        0 = valid url
        1 = cannot access or parse the page after a first successful get request
        2 = page cannot access - 403/401, then should verify if it is indeed access issue or due to robot webscraping
        3 = other status code between 400 - 500 except 404, 403, 401
        4 = url server down?/ not found - 500/404
        5 = url doesn't exist in DNS - connection error
        6 = server not responding - time out
        """
        logger.info('_check_url() %s', url)

        retry_limit = 2
        number_try = 0
        connection_error_count = 0
        timeout_error_count = 0

        while number_try < retry_limit:
            try:
                r = requests.head(url, allow_redirects=True, timeout=4)
                logger.info('status %i', r.status_code)

                # go into granular categorization if error code
                if r.status_code >= 400:
                    if r.status_code >= 500 or r.status_code == 404:
                        return 4
                    elif r.status_code == 403 or r.status_code == 401:
                        return 2
                    else:
                        return 3
                # else return success code
                return 0
            except (requests.ConnectionError, requests.Timeout) as e:
                logger.warning(e)
                # increment retry and find out what error it is
                number_try += 1
                if isinstance(e, requests.ConnectionError):
                    connection_error_count += 1
                else:
                    timeout_error_count += 1

        return 5 if connection_error_count >= timeout_error_count else 6

    # ------------ validation ------------------ #

    def validate(self, passage_context: PassageContext):
        logger.info('validate() %s', passage_context)
        # check if curr_soup is ready
        if (self.curr_soup is None):
            raise Exception('soup is not cooked')

        validate_result_list: list[ValidationResult] = []
        # perform validation for each context
        for k, v in passage_context.items():
            if (not v):
                continue
            curr_validate_context_result = self._validate_context_controller(
                k, v)
            if (self._validate_evaluator(curr_validate_context_result['scores'])):
                curr_validate_context_result['validation_code'] = 0
                return curr_validate_context_result
            if (len(curr_validate_context_result.get('scores')) > 0):
                validate_result_list.append(curr_validate_context_result)

        # find the best result among all contexts

        # in case result list is empty
        if (len(validate_result_list) == 0):
            return {'validation_code': 1}
        best_index = 0
        best_score = 0
        for i, validate_result in enumerate(validate_result_list):
            curr_score = sum(
                validate_result['scores']) / len(validate_result['scores'])
            if best_score < curr_score:  # compare best score with curr score
                best_score = curr_score
                best_index = i

        best_result = validate_result_list[best_index]
        best_result['validation_code'] = 0

        return best_result

    # interal validate methods
    def _validate_context_controller(self, context: str, input: str) -> ValidationResult:
        logger.info('_validate_context_controller() %s', context)

        keywords: list[str] = pos_phrase(
            input) if context == 'linked_str' else keywords_extractor(input)['words']
        num_keywords = len(keywords)

        if (num_keywords == 0):
            return {'keywords': [], 'scores': []}

        scores_set: list[list[float]] = []
        # title validation
        if (context == 'linked_str'):
            titles = self._get_title()
            logger.info('_validate_context_controller() titles: %s', titles)
            scores_title = [0] * num_keywords
            # check if titles contain these keywords
            for i, keyword in enumerate(keywords):
                keyword_lowercase = keyword.lower()
                for title in titles:
                    if (keyword_lowercase in title):
                        scores_title[i] = 1
            # push title scores into scores_set
            scores_set.append(scores_title)

        # summary validation
        summary = self._get_summary()
        if (summary and summary != foo):
            classification_summary = classifier(summary, keywords)
            scores_set.append(classification_summary['scores'])

        # body validation
        body = self._get_cleaned_body()
        if (body and body != foo):
            classification_body = classifier(body, keywords)
            scores_set.append(classification_body['scores'])

        # find best among these validation for each words
        best_set = []
        # if scores_set is empty, return empty scores
        if (len(scores_set) == 0):
            return {'keywords': keywords, 'scores': best_set}
        for i in range(num_keywords):
            best = max([score_set[i] for score_set in scores_set])
            best_set.append(best)

        return {'keywords': keywords, 'scores': best_set}

    def _validate_evaluator(self, scores: list[float]):
        logger.info('_validate_evaluator() %s', scores)
        if (len(scores) == 0):
            return False
        sum = 0
        for score in scores:
            if (score == 1):
                return True
            sum += score

        return (sum / len(scores)) > 0.95

    # ----------- internal parsing methods -------------- #
    def _get_title(self):
        logger.info('_get_title()')

        if (self.curr_url.get('title')):
            return self.curr_url.get('title')

        soup = self.curr_soup
        possible_titles: list[str] = []

        str_dom = str(soup)
        self.curr_doc = Document(str_dom)
        read_title = self.curr_doc.title()

        if (read_title):
            possible_titles.append(read_title.lower())

        # find all possible titles in head
        head = soup.find('head')
        if (head is None):
            self.curr_url['title'] = possible_titles
            return self.curr_url['title']
        soup_titles: ResultSet[Tag] = head.find_all(filter_title)

        # push lowercased string in titles into possible_titles
        for title in soup_titles:
            if (title.name == 'title'):
                possible_titles.append(title.string.lower())
            else:
                possible_titles.append(title['content'].lower())

        self.curr_url['title'] = possible_titles

        return self.curr_url['title']

    def _get_summary(self) -> str:
        logger.info('_get_summary()')

        if (self.curr_url.get('summary')):
            return self.curr_url.get('summary')

        soup = self.curr_soup
        head = soup.find('head')
        if (head is None):
            self.curr_url['summary'] = foo
            return self.curr_url['summary']

        tag_description: (Tag | None) = head.find(filter_description)

        self.curr_url['summary'] = foo if tag_description is None else tag_description['content']

        return self.curr_url['summary']

    def _get_cleaned_body(self):
        logger.info('_get_cleaned_body()')

        if (self.curr_url.get('body')):
            return self.curr_url.get('body')

        read_doc_content = self.curr_doc.summary(html_partial=True)
        body = ''
        # find content
        if (read_doc_content is not None):
            content_soup = BeautifulSoup(read_doc_content, "lxml")
            punctuation = {'.', ',', '?', '!', ':', ';'}
            body = ''
            for string in content_soup.stripped_strings:
                if (not string):
                    continue
                first_letter = string[0]
                if (first_letter in punctuation):
                    body += string
                else:
                    body += ' ' + string

        self.curr_url['body'] = foo if body == '' else body

        return self.curr_url['body']
