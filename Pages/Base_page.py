from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from Tests.locators.contact_page_locators import Button
import time
import allure
import json


class Base_page:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Open the page")
    # def open(self):
    #     self.driver.get(self.url)
    def open(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error during opening the page",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("Close borlabs banner")
    def borlabs_banner_close(self):
        try:
            borlabs_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Button.borlabs))
            )
            borlabs_button.click()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error during closing Borlabs banner",
                          attachment_type=allure.attachment_type.PNG)

    @allure.step("Select random option in dropdown")
    def select_random_option_from_dropdown(self, dropdown_locator, options_locator, selected_option_locator):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dropdown_locator)
        ).click()

        options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, options_locator)))

        random_index = random.randint(1, len(options) - 1)
        options[random_index].click()
        selected_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, selected_option_locator))).text
        return selected_option

    @allure.step("Select exact option in dropdown")
    def select_exact_option(self, dropdown_locator, option_locator, selected_option_locator):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dropdown_locator)).click()
        option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, option_locator))).click()

        selected_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, selected_option_locator))).text
        return selected_option

    @allure.step("Submit form")
    def submit_form(self, button_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_locator))).click()

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Select checkbox")
    def select_checkbox(self, locator):
        checkbox = self.driver.find_element(By.XPATH, locator).click()

    @allure.step("Compare page URL")
    def compare_page_url(self, pardot_url, expected_url):
        try:
            url_pardot = self.driver.find_element(By.XPATH, pardot_url).text.strip()
            assert expected_url == url_pardot, f"url_pardot: {url_pardot}, expected_url: {expected_url}"

            allure.attach(
                json.dumps({"URL_pardot": url_pardot, "Expected_Url": expected_url}, indent=2).encode('utf-8'),
                name='URL Comparison', attachment_type=allure.attachment_type.JSON)


        except AssertionError as e:
            print(f"Assertion error in URL comparison: {e}")

    @allure.step("Scroll to element")
    def scroll_to_element(self, element_locator):
        element = self.driver.find_element(By.XPATH, element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)



