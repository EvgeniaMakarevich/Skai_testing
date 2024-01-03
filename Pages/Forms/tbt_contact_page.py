from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.locators.tbt_locators import ContactForm
from faker import Faker
from Pages.Base_page import Base_page
from Tests.data.tbt_data import Json_path
import time
import json
import os
import shutil

fake = Faker()
class TbtContact(Base_page):
    def scroll_to_form(self,driver):
        element = driver.find_element(*ContactForm.scroll_to_form)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)


    def fill_form(self,driver):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ContactForm.button_modal_window)).click()
        modal_window = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ContactForm.modal_window))

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ContactForm.first_name_field)).send_keys('Internal test')
        self.entered_name = 'Internal test'

        email = fake.email()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ContactForm.email_address_field)).send_keys(email)
        self.entered_email = email

        last_name = fake.last_name()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ContactForm.last_name_field)).send_keys(last_name)
        self.entered_last_name = last_name

        text_c = fake.text()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ContactForm.message_field)).send_keys(text_c)
        self.entered_text_c = text_c
        time.sleep(2)
    def get_entered_data(self):
        return {
            'name': getattr(self, 'entered_name', None),
            'email': getattr(self, 'entered_email', None),
            'last_name': getattr(self, 'entered_last_name', None),
            'text_c': getattr(self, 'entered_text_c', None)
        }

    def submit_tbt_form(self,driver):
        driver.find_element(ContactForm.submit_button).click()


    def fill_tbt_form(self,driver):
        self.scroll_to_form(driver)
        time.sleep(2)
        self.fill_form(driver)
        entered_data = self.get_entered_data()

        with open('entered_data_tbt_contact', 'w') as file:
            json.dump(entered_data, file)
        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, Json_path.tbt_contact)
        shutil.move('entered_data_tbt_contact', destination_directory)


