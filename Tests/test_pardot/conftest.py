import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Tests.data.pardot_data import Pardot_data
from Tests.locators.pardot_locators import Pardot_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pyotp import *
import allure


@pytest.fixture(scope='session')
def options():
    options = Options()
    options.add_argument('--headless')
    return options

@pytest.fixture(scope='session')
def browser(options):
    chrome_service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=chrome_service, options=options)
    # browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()

@allure.step('Login')
@pytest.fixture(scope='session')
# @pytest.fixture(scope='function')
def get_pardot(browser):
    browser.get(Pardot_data.pardot_main)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, Pardot_locators.username))).send_keys(Pardot_data.username_data)
    browser.find_element(By.XPATH, Pardot_locators.password).send_keys(Pardot_data.password_data)

    browser.find_element(By.XPATH, Pardot_locators.log_in).click()

    time.sleep(3)
    totp = TOTP("")
    token = totp.now()

    WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH, Pardot_locators.verification_field))).send_keys(token)
    browser.find_element(By.XPATH, Pardot_locators.save_button).click()

    browser.get(Pardot_data.log_in_page)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, Pardot_locators.log_in_sf_button))).click()
    time.sleep(3)
    yield browser
