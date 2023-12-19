import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Tests.data.pardot_data import Pardot_data
from Tests.locators.pardot_locators import Pardot_locators
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()




