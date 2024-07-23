from bs4 import BeautifulSoup, Tag, ResultSet
from readability import Document

def get_title(soup: BeautifulSoup):
  print("get_title()")
  
  possible_titles: list[str] = []
  
  str_dom = str(soup)
  read_title = Document(str_dom).title()
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
  
  return possible_titles

def get_summary(soup: BeautifulSoup):
  print("get_summary()")
  head = soup.find('head')
  tag_description = head.find(filter_description)
  
  return tag_description['content']
  


def get_cleaned_body(soup: BeautifulSoup):
  print("get_cleaned_body():")
  str_dom = str(soup)
  read_doc_content = Document(str_dom).summary(html_partial=True)
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
    
  return body

# def parse(soup: BeautifulSoup):
#   result = {}
#   # parse using readability 
#   str_dom = str(soup)
#   read_doc = Document(str_dom)
#   read_doc_title = read_doc.title()
#   read_doc_content = read_doc.summary(html_partial=True)
#   if (read_doc_title):
#     result['title'] = read_doc_title
  
#   # parse using beautiful soup
#   head: Tag = soup.find('head')

#   # if we don't have title from readability, find title using soup
#   if (result.get('title') is None):
#     soup_title = head.find(filter_title)
#     if (soup_title):
#       result['title'] = soup_title['content'] if soup_title.name == 'meta' else soup_title.get_text()

#   # find description/summary
#   description = head.find(filter_description)
#   if (description):
#     result['summary'] = description['content'] if description.name == 'meta' else description.get_text()
    
#   # find content
#   if (read_doc_content is not None):
#     content_soup = BeautifulSoup(read_doc_content, "lxml")
#     punctuation = {'.', ',', '?', '!', ':', ';'}
#     body = ''
#     for string in content_soup.stripped_strings:
#       if (not string):
#         continue
#       first_letter = string[0]
#       if (first_letter in punctuation):
#         body += string
#       else:
#         body += ' ' + string
    
#     result['body'] = body

    
#   return result

'''
find title of the webpage
  1. <title> tag
  2. <meta> tag with attribute name/property contains title
'''
def filter_title(tag: Tag):
  # 1. <title> tag
  if (tag.name == 'title' and tag.string):
    return True
  
  # 2. <meta> tag with attribute name/property contains title
  if (tag.name == 'meta'):
    name_attr = tag.attrs.get('name') or ''
    property_attr = tag.attrs.get('property') or ''
    content_attr = tag.attrs.get('content') or ''
    return content_attr != '' and (('title' in name_attr) or ('title' in property_attr))
  
  return False

def filter_description(tag: Tag):
  # if it is not meta, return false
  if tag.name != 'meta':
    return False
  # if it is not meta or no content, return false
  content_attr: str = tag.attrs.get('content') or ''
  name_attr: str = tag.attrs.get('name') or ''
  property_attr: str = tag.attrs.get('property') or ''
  
  return content_attr != '' and (('description' in name_attr) or ('description' in property_attr))
  
  