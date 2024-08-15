import subprocess
import os
from selenium import webdriver
from tempfile import mkdtemp


def create_driver():
    env = os.environ.get('ENV_VAR', 'localhost')

    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService() if env == 'localhost' else webdriver.ChromeService(executable_path='/opt/chromedriver', service_args=[
        '--log-level=INFO'], log_output=subprocess.STDOUT)

    options.page_load_strategy = 'eager'

    if (env != 'localhost'):
        options.binary_location = '/opt/chrome/chrome'

        # options.add_argument("--headless=new")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        # options.add_argument("--window-size=800x600")
        options.add_argument('--disable-default-apps')
        options.add_argument('--disable-extensions')
        options.add_argument(
            '--disable-features=InterestFeedContentSuggestions')
        options.add_argument('--disable-features=Translate')
        options.add_argument('--mute-audio')
        options.add_argument('--ash-no-nudges')
        options.add_argument('--enable-automation')
        options.add_argument('--disable-notifications')

        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-dev-tools")
        options.add_argument("--no-zygote")
        options.add_argument(f"--user-data-dir={mkdtemp()}")
        options.add_argument(f"--data-path={mkdtemp()}")
        # options.add_argument(f"--profile-directory={mkdtemp()}")
        options.add_argument(f"--disk-cache-dir={mkdtemp()}")
        options.add_argument("--remote-debugging-port=9222")

    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=service)
    driver.set_page_load_timeout(6)

    return driver
