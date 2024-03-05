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

    # events with fields  name, last_name, email, phone, company,job_title, country, state, dietary_requirements
    @allure.step('Fill event form')
    def fill_form_1(self, name_locator, last_name_locator, email_locator, phone_locator, company_name_locator,
                  job_title_locator,
                  country_locator, country_option_usa, country_soptions, state_locator, state_options, state_soption,
                  dietary_req_locator):
        try:
            with allure.step("Entering name"):
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(name_locator)).send_keys(
                    'Internal test')
                self.entered_name = 'Internal test'
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering name",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Entering email"):
                email = fake.email()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_locator)).send_keys(email)
                self.entered_email = email
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering email",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Entering last name"):
                last_name = fake.last_name()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(last_name_locator)).send_keys(last_name)
                self.entered_last_name = last_name
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering last name",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Entering phone"):
                phone = fake.phone_number()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(phone_locator)).send_keys(phone)
                self.entered_phone = phone
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering phone",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Entering company name"):
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(company_name_locator)).send_keys(
                    'Dizzain')
                self.entered_company_name = 'Dizzain'
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering company name",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Entering job title"):
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(job_title_locator)).send_keys('QA')
                self.entered_job_title = 'QA'
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering job title",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Choose USA option in 'Country' dropdown"):
                country_option = self.select_exact_option(country_locator, country_option_usa, country_soptions)
                self.entered_country = country_option
                allure.attach(self.driver.get_screenshot_as_png(), name="Choose USA option in 'Country' dropdown",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Choose random option in 'State' dropdown"):
                state_option = self.select_random_option_from_dropdown(state_locator, state_options, state_soption)
                self.entered_state = state_option
                allure.attach(self.driver.get_screenshot_as_png(), name="Choose random option in 'State' dropdown",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Enter text in 'Dietary requirements' field"):
                dietary_req = fake.text()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(dietary_req_locator)).send_keys(dietary_req)
                self.entered_dietary_req = dietary_req
                allure.attach(self.driver.get_screenshot_as_png(), name="Enter text in 'Dietary requirements' field",
                              attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error on form filling",
                          attachment_type=allure.attachment_type.PNG)
            raise e

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
    def get_and_save_entered_report_data_1(self, filename, destination_path):
        entered_data = self.get_entered_data()

        with allure.step("Save entered data to Allure"):
            allure.attach(json.dumps(entered_data, indent=2), name="Entered Data",
                          attachment_type=allure.attachment_type.JSON)

        with open(filename, 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, destination_path)
        shutil.move(filename, destination_directory)



    # events with fields  name, last_name, email, company,job_title,
    # "What are you interested in? dropdown", "What would you like to discuss?" dropdown
    @allure.step('Fill event form')
    def fill_form_2(self, name_locator, last_name_locator, email_locator, company_name_locator,
                  job_title_locator,
                  what_interested_in_locator, what_interested_in_options, what_interested_in_soption,
                  what_to_discuss_locator):
        try:
            with allure.step("Entering name"):
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(name_locator)).send_keys(
                    'Internal test')
                self.entered_name = 'Internal test'
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering name",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Entering email"):
                email = fake.email()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_locator)).send_keys(email)
                self.entered_email = email
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering email",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Entering last name"):
                last_name = fake.last_name()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(last_name_locator)).send_keys(last_name)
                self.entered_last_name = last_name
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering last name",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Entering company name"):
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(company_name_locator)).send_keys(
                    'Dizzain')
                self.entered_company_name = 'Dizzain'
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering company name",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Entering job title"):
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(job_title_locator)).send_keys('QA')
                self.entered_job_title = 'QA'
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering job title",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Choose random option in 'What are you interested in?' dropdown"):
                what_interested_in = self.select_random_option_from_dropdown(what_interested_in_locator, what_interested_in_options, what_interested_in_soption)
                self.entered_what_interested_in= what_interested_in
                allure.attach(self.driver.get_screenshot_as_png(), name="Choose random option in 'What are you interested in?' dropdown",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Enter text in 'What would you like to discuss?' field"):
                what_to_discuss = fake.text()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(what_to_discuss_locator)).send_keys(
                    what_to_discuss)
                self.entered_what_to_discuss = what_to_discuss
                allure.attach(self.driver.get_screenshot_as_png(), name="Enter text in 'What would you like to discuss?' field",
                              attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error on form filling",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    def get_entered_data_2(self):
        return {
            'name': getattr(self, 'entered_name', None),
            'email': getattr(self, 'entered_email', None),
            'last_name': getattr(self, 'entered_last_name', None),
            'company_name': getattr(self, 'entered_company_name', None),
            'job_title': getattr(self, 'entered_job_title', None),
            'what_interested_in': getattr(self, 'entered_what_interested_in', None),
            'what_to_discuss': getattr(self, 'entered_what_to_discuss', None)
        }

    @allure.step("Get and save entered data")
    def get_and_save_entered_report_data_2(self, filename, destination_path):
        entered_data = self.get_entered_data_2()

        with allure.step("Save entered data to Allure"):
            allure.attach(json.dumps(entered_data, indent=2), name="Entered Data",
                          attachment_type=allure.attachment_type.JSON)

        with open(filename, 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, destination_path)
        shutil.move(filename, destination_directory)