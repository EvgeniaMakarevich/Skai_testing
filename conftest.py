import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def options():
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    return options



@pytest.fixture(scope='function')
def driver(options):
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()




