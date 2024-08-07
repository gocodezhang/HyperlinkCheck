from selenium import webdriver
import time


def create_driver():
    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService(executable_path='/opt/chromedriver')

    options.binary_location = '/opt/chrome/chrome'

    options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)

    options.add_argument('--disable-default-apps')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-features=InterestFeedContentSuggestions')
    options.add_argument('--disable-features=Translate')
    options.add_argument('--mute-audio')
    options.add_argument('--ash-no-nudges')
    options.add_argument('--enable-automation')
    options.add_argument('--disable-notifications')

    driver = webdriver.Chrome(options=options, service=service)
    driver.set_page_load_timeout(6)

    return driver
