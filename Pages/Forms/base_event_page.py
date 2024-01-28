from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from Pages.Base_page import Base_page
import allure
import json
import os
import shutil

fake = Faker()

class BaseEventPage(Base_page):

    # Event with phone and dietary requirements
    def fill_form(self, name_locator, last_name_locator, email_locator, phone_locator, company_name_locator, job_title_locator,
                  country_locator, country_option_usa, country_soptions, state_locator,state_options,state_soption, dietary_req_locator):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(name_locator)).send_keys('Internal test')
        self.entered_name = 'Internal test'

        email = fake.email()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_locator)).send_keys(email)
        self.entered_email = email

        last_name = fake.last_name()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(last_name_locator)).send_keys(last_name)
        self.entered_last_name = last_name

        phone = fake.phone_number()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(phone_locator)).send_keys(phone)
        self.entered_phone = phone

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(company_name_locator)).send_keys('Dizzain')
        self.entered_company_name = 'Dizzain'

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(job_title_locator)).send_keys('QA')
        self.entered_job_title = 'QA'

        country_option = self.select_exact_option(country_locator, country_option_usa, country_soptions)
        self.entered_country = country_option

        state_option = self.select_random_option_from_dropdown(state_locator, state_options, state_soption)
        self.entered_state = state_option

        dietary_req = fake.text()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(dietary_req_locator)).send_keys(dietary_req)
        self.entered_dietary_req = dietary_req


    def get_entered_data(self):
        return {
            'name': getattr(self, 'entered_name', None),
            'email': getattr(self, 'entered_email', None),
            'last_name': getattr(self, 'entered_last_name', None),
            'company_name': getattr(self, 'entered_company_name', None),
            'job_title': getattr(self, 'entered_job_title', None),
            'phone': getattr(self, 'entered_phone', None),
            'country': getattr(self, 'entered_country', None),
            'state': getattr(self, 'entered_state', None),
            'dietary_req': getattr(self, 'entered_dietary_req', None)
        }

    @allure.step("Get and save entered data")
    def get_and_save_entered_report_data(self, filename, destination_path):
        entered_data = self.get_entered_data()
        with open(filename, 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, destination_path)
        shutil.move(filename, destination_directory)