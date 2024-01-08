from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from Tests.locators.contact_page_locators import Button
import time


class Base_page:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.url)

    def borlabs_banner_close(self):
        borlabs_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Button.borlabs))
        )
        borlabs_button.click()

    def select_random_option_from_dropdown(self, dropdown_locator, options_locator, selected_option_locator):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dropdown_locator)
        ).click()

        options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, options_locator)))

        random_index = random.randint(1, len(options) - 1)
        options[random_index].click()
        # options[1].click()
        selected_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, selected_option_locator))).text
        return selected_option

    def select_exact_option(self, dropdown_locator, option_locator, selected_option_locator):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dropdown_locator)).click()
        option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, option_locator))).click()

        # self.driver.execute_script("window.scrollBy(0, 200);")
        # time.sleep(3)
        # option = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, option_locator)))
        # option.click()

        selected_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, selected_option_locator))).text
        # EC.visibility_of_element_located((By.XPATH, selected_option_locator))).text
        return selected_option

    def submit_form(self, button_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_locator))).click()

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def select_checkbox(self, locator):
        checkbox = self.driver.find_element(By.XPATH, locator).click()

    def compare_page_url(self, pardot_url, expected_url):
        url_pardot = self.driver.find_element(By.XPATH, pardot_url).text.strip()
        assert expected_url == url_pardot, f"url_pardot: {url_pardot},expected_url: {expected_url}"

    def scroll_to_element(self, element_locator):
        element = self.driver.find_element(By.XPATH, element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
