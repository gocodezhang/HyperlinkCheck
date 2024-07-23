from selenium import webdriver

def create_driver():
  options = webdriver.ChromeOptions()
  options.page_load_strategy = 'eager'
  options.add_experimental_option("detach", True)
  driver = webdriver.Chrome(options=options)
  return driver

# def exclude_script_tag(tag_name, attrs):
#   # tag_name != 'script' and tag_name != 'style' and tag_name != 'svg' and tag_name != 'link'
#   print(tag_name)
#   print(attrs)
#   return tag_name == 'p'