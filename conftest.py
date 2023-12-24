import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# @pytest.fixture
# def options():
#     options = Options()
#     options.add_argument('--window-size=2880,2800')
#     return options

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()




