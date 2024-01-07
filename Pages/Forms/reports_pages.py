from selenium.webdriver.common.by import By
from Pages.Forms.base_reports_page import BaseReportPage
from Tests.locators.contact_page_locators import Fields_locators
from Tests.data.reports_pages_data import Json_path
from Tests.locators.sem_pages_locators import Checkbox
import time
import json
import os
import shutil


class ReportsPages(BaseReportPage):
    def fill_hidden_cost(self, driver):
        # element = driver.find_element(By.XPATH, Fields_locators.contact_form)
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        self.scroll_to_element(Fields_locators.contact_form)

        time.sleep(2)

        self.fill_form(Fields_locators.name_input,
                       Fields_locators.email_input,
                       Fields_locators.lastname_input,
                       Fields_locators.company_input,
                       Fields_locators.job_title_input)

        self.select_checkbox(Checkbox.checkbox)

        entered_data = self.get_entered_data()
        with open('entered_data_hidden_cost_report', 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, Json_path.hidden_cost_report)
        shutil.move('entered_data_hidden_cost_report', destination_directory)

    def fill_ai(self, driver):
        # element = driver.find_element(By.XPATH, Fields_locators.contact_form)
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        self.scroll_to_element(Fields_locators.contact_form)

        time.sleep(2)

        self.fill_form(Fields_locators.name_input,
                       Fields_locators.email_input,
                       Fields_locators.lastname_input,
                       Fields_locators.company_input,
                       Fields_locators.job_title_input)

        self.select_checkbox(Checkbox.checkbox)

        entered_data = self.get_entered_data()
        with open('entered_data_ai_report', 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, Json_path.ai_report)
        shutil.move('entered_data_ai_report', destination_directory)

    def fill_prime_day(self, driver):
        # element = driver.find_element(By.XPATH, Fields_locators.contact_form)
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        self.scroll_to_element(Fields_locators.contact_form)

        time.sleep(2)

        self.fill_form(Fields_locators.name_input,
                       Fields_locators.email_input,
                       Fields_locators.lastname_input,
                       Fields_locators.company_input,
                       Fields_locators.job_title_input)

        self.select_checkbox(Checkbox.checkbox)

        entered_data = self.get_entered_data()
        with open('entered_data_prime_day_report', 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, Json_path.prime_day_report)
        shutil.move('entered_data_prime_day_report', destination_directory)


    def fill_amazon_playbook(self, driver):
        # element = driver.find_element(By.XPATH, Fields_locators.contact_form)
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        self.scroll_to_element(Fields_locators.contact_form)

        time.sleep(2)

        self.fill_form(Fields_locators.name_input,
                       Fields_locators.email_input,
                       Fields_locators.lastname_input,
                       Fields_locators.company_input,
                       Fields_locators.job_title_input)

        self.select_checkbox(Checkbox.checkbox)

        entered_data = self.get_entered_data()
        with open('entered_data_amazon_playbook_report', 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, Json_path.amazon_playbook_report)
        shutil.move('entered_data_amazon_playbook_report', destination_directory)


    def fill_apple_ads(self, driver):
        # element = driver.find_element(By.XPATH, Fields_locators.contact_form)
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        self.scroll_to_element(Fields_locators.contact_form)

        time.sleep(2)

        self.fill_form(Fields_locators.name_input,
                       Fields_locators.email_input,
                       Fields_locators.lastname_input,
                       Fields_locators.company_input,
                       Fields_locators.job_title_input)

        self.select_checkbox(Checkbox.checkbox)

        entered_data = self.get_entered_data()
        with open('entered_data_apple_ads_report', 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, Json_path.apple_ads_report)
        shutil.move('entered_data_apple_ads_report', destination_directory)
