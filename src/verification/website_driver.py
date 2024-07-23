from selenium import webdriver
import time

def create_driver():
  start = time.time()
  options = webdriver.ChromeOptions()
  options.page_load_strategy = 'eager'
  options.add_experimental_option("detach", True)
  
  options.add_argument('--disable-default-apps')
  options.add_argument('--disable-extensions')
  options.add_argument('--disable-features=InterestFeedContentSuggestions')
  options.add_argument('--mute-audio')
  options.add_argument('--mute-audio')
  options.add_argument('--mute-audio')
  options.add_argument('--ash-no-nudges')
  options.add_argument('--enable-automation')
  
  driver = webdriver.Chrome(options=options)
  print('create driver: ', time.time() - start)
  return driver