import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Tests.data.pardot_data import Pardot_data
from Tests.locators.pardot_locators import Pardot_locators
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope='session',autouse=True)
def get_pardot(browser):
    browser.get(Pardot_data.pardot_main)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, Pardot_locators.username))).send_keys(Pardot_data.username_data)
    browser.find_element(By.XPATH, Pardot_locators.password).send_keys(Pardot_data.password_data)

    browser.find_element(By.XPATH, Pardot_locators.log_in).click()
    WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH, Pardot_locators.verification_field))).send_keys(Pardot_data.verification_code)
    browser.find_element(By.XPATH, Pardot_locators.save_button).click()

    browser.get(Pardot_data.log_in_page)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, Pardot_locators.log_in_sf_button))).click()
    time.sleep(3)
    yield browser
