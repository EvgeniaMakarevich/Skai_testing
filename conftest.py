import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope='function')
def options():
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    return options



@pytest.fixture(scope='function')
def driver(options):
    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)
    # driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()




