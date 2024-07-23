from bs4 import BeautifulSoup, Tag, ResultSet
from readability import Document
from verification.website_driver import create_driver
from verification.parse_helper import filter_title, filter_description
from nlp import classifier, keywords_extractor, find_nouns

class HyperlinkVerifier:
  
  # constructor
  def __init__(self):
    self.webdriver = create_driver()
    self.curr_soup: (BeautifulSoup | None) = None
    self.curr_doc: (Document | None) = None
    self.curr_url = {}
    return 
  
  def read_url(self, url: str):
    print('read_url(): ', url)
    
    # clean up previous url data
    self.curr_url.clear()
    self.curr_doc = None
    self.curr_soup = None

    # open url
    self.webdriver.get(url)
    # read the source page
    html = self.webdriver.page_source
    # parse html into string
    soup = BeautifulSoup(html, "lxml")
    self.curr_soup = soup
    return
  
  def validate(self, passage_context):
    return self.__validate_stage_controller('linked_str', passage_context['linked_str'])
  
  # validate methods
  def __validate_stage_controller(self, stage: str, input: str):
    print("validate_stage_controller()")
    
    keywords = find_nouns(input) if stage == 'linked_str' else keywords_extractor(input)['words']
    num_keywords = len(keywords)
    scores_set: list[list[float]] = []
    # title validation
    if (stage == 'linked_str'):
      titles = self.__get_title()
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
    summary = self.__get_summary()
    print('article: ' + summary)
    if summary:
      classification_summary = classifier(summary, keywords)
      print('classification: ', str(classification_summary))
      scores_set.append(classification_summary['scores'])
    
    # body validation
    body = self.__get_cleaned_body()
    print('body: ', body)
    if body:
      classification_body = classifier(body, keywords)
      print('classification: ', str(classification_body))
      scores_set.append(classification_body['scores'])
    
    # find best among these validation for each words
    best_set = []
    for i in range(num_keywords):
      best = max([score_set[i] for score_set in scores_set])
      best_set.append(best)
        
  
    return {'keywords': keywords, 'scores': best_set}
    
  
  # internal parsing methods
  def __get_title(self):
    print("get_title()")
    
    if (self.curr_url.get('title')):
      return self.curr_url.get('title')
    
    soup = self.curr_soup
    possible_titles: list[str] = []
    
    str_dom = str(soup)
    self.curr_doc = Document(str_dom)
    read_title = self.curr_doc.title()
    print('get_title():read_title: ' + read_title)
    
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
  
  def __get_summary(self):
    print("get_summary()")
    soup = self.curr_soup
    head = soup.find('head')
    tag_description = head.find(filter_description)
    
    self.curr_url['summary'] = tag_description['content']
    
    return self.curr_url['summary']
  
  def __get_cleaned_body(self):
    print("get_cleaned_body():")
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