from bs4 import BeautifulSoup, Tag, ResultSet
from readability import Document
from verification.website_driver import create_driver
from verification.parse_helper import filter_title, filter_description
from nlp import classifier, keywords_extractor, pos_phrase
import time
import logging

logger = logging.getLogger('HyperlinkVerifier')
logging.basicConfig(level=logging.INFO)

class HyperlinkVerifier:
  
  # ------------ constructor ------------------ #
  def __init__(self):
    self.webdriver = create_driver()
    self.curr_soup: (BeautifulSoup | None) = None
    self.curr_doc: (Document | None) = None
    self.curr_url = {}
    return 
  
  # ------------ read ------------------ #
  def read_url(self, url: str):
    logger.info('read_url() %s' + url)
    
    # clean up previous url data
    self.curr_url.clear()
    self.curr_doc = None
    self.curr_soup = None

    # open url
    start = time.time()
    self.webdriver.get(url)
    logger.info('reading time: %f', time.time() - start)
    # read the source page
    html = self.webdriver.page_source
    # parse html into string
    soup = BeautifulSoup(html, "lxml")
    self.curr_soup = soup
    return
  
  # ------------ validate url with passage ------------------ #
  def validate(self, passage_context: dict[str, str]):
    logger.info('validate() %s', passage_context)
    validate_result_list: list[dict[str, list]] = []
    # perform validation for each context
    for k, v in passage_context.items():
      curr_validate_context_result = self._validate_context_controller(k, v)
      if (self._validate_evaluator(curr_validate_context_result['scores'])):
        return curr_validate_context_result
      validate_result_list.append(curr_validate_context_result)
    
    # find the best result among all contexts
    best_index = 0
    best_score = 0
    for i, validate_result in enumerate(validate_result_list):
      curr_score = sum(validate_result['scores']) / len(validate_result['scores'])
      if best_score < curr_score: # compare best score with curr score
        best_score = curr_score
        best_index = i
    
    return validate_result_list[best_index]
  
  # interal validate methods
  def _validate_context_controller(self, context: str, input: str):
    logger.info("validate_context_controller() %s", context)
    
    keywords = pos_phrase(input) if context == 'linked_str' else keywords_extractor(input)['words']
    num_keywords = len(keywords)
    scores_set: list[list[float]] = []
    # title validation
    if (context == 'linked_str'):
      titles = self._get_title()
      logger.info('titles %s', titles)
      scores_title = [0] * num_keywords
      # check if titles contain these keywords
      for i, keyword in enumerate(keywords):
        for title in titles:
          if (keyword in title):
            scores_title[i] = 1
            break
      # push title scores into scores_set
      scores_set.append(scores_title)
  
    # summary validation
    summary = self._get_summary()
    logger.info('summary %s', summary)
    if summary:
      classification_summary = classifier(summary, keywords)
      scores_set.append(classification_summary['scores'])
    
    # body validation
    body = self._get_cleaned_body()
    logger.info('body %s', body)
    if body:
      classification_body = classifier(body, keywords)
      scores_set.append(classification_body['scores'])
    
    # find best among these validation for each words
    best_set = []
    for i in range(num_keywords):
      best = max([score_set[i] for score_set in scores_set])
      best_set.append(best)
        
  
    return {'keywords': keywords, 'scores': best_set}
    
  def _validate_evaluator(self, scores: list[float]):
    sum = 0
    for score in scores:
      if (score == 1):
        return True
      sum += score
      
    return (sum / len(scores)) > 0.95
  
  # ----------- internal parsing methods -------------- #
  def _get_title(self):
    
    if (self.curr_url.get('title')):
      return self.curr_url.get('title')
    
    soup = self.curr_soup
    possible_titles: list[str] = []
    
    str_dom = str(soup)
    self.curr_doc = Document(str_dom)
    read_title = self.curr_doc.title()
    
    if (read_title):
      possible_titles.append(read_title)
      
    # find all possible titles in head
    head: Tag = soup.find('head')
    soup_titles: ResultSet[Tag] = head.find_all(filter_title)
    
    # push string in titles into possible_titles
    for title in soup_titles:
      if (title.name == 'title'):
        possible_titles.append(title.string)
      else:
        possible_titles.append(title['content'])
    
    self.curr_url['title'] = possible_titles
    
    return self.curr_url['title']
  
  def _get_summary(self):
    soup = self.curr_soup
    head = soup.find('head')
    tag_description = head.find(filter_description)
    
    self.curr_url['summary'] = tag_description['content']
    
    return self.curr_url['summary']
  
  def _get_cleaned_body(self):
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
    
    self.curr_url['body'] = body  
    
    return self.curr_url['body']