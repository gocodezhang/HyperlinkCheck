from bs4 import Tag

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
