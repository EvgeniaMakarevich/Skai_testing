from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from Pages.Base_page import Base_page
import time
import allure
import json
import os
import shutil

fake = Faker()


class ContactPage(Base_page):
    @allure.step("Fill the form")
    def fill_form(self, name_locator, email_locator, last_name_locator, company_name_locator, job_title_locator,
                  area_of_int_locator, area_of_int_options, area_of_int_soption, m_dig_spend_locator,
                  m_dig_spend_options, m_dig_spend_soption, country_locator, country_option_usa, country_soptions,
                  state_locator, state_options, state_soption, text_c_locator, how_heard_locator, how_heard_options,
                  how_heard_soption, other_field_locator):
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

            time.sleep(3)

            with allure.step("Choose option in 'Area of Interest' dropdown"):
                area_of_int_option = self.select_random_option_from_dropdown(area_of_int_locator, area_of_int_options,
                                                                                  area_of_int_soption)
                self.entered_area_of_int = area_of_int_option
                allure.attach(self.driver.get_screenshot_as_png(), name="Choose option in 'Area of Interest' dropdown",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Choose option in 'Monthly Digital spend' dropdown"):
                m_dig_spend_option = self.select_random_option_from_dropdown(m_dig_spend_locator, m_dig_spend_options,m_dig_spend_soption)
                self.entered_m_dig_spend = m_dig_spend_option
                allure.attach(self.driver.get_screenshot_as_png(), name="Choose option in 'Monthly Digital spend' dropdown",
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

            with allure.step("Entering text_c"):
                text_c = fake.text()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(text_c_locator)).send_keys(text_c)
                self.entered_text_c = text_c
                allure.attach(self.driver.get_screenshot_as_png(), name="Entering text_c",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Choose 'Other' option in 'How heard about us' dropdown"):
                how_heard_option = self.select_exact_option(how_heard_locator, how_heard_options, how_heard_soption)
                self.entered_how_heard = how_heard_option
                allure.attach(self.driver.get_screenshot_as_png(), name="Choose 'Other' option in 'How heard about us' dropdown",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Enter text in 'Other' field"):
                text_other = fake.text()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(other_field_locator)).send_keys(text_other)
                self.entered_text_other = text_other
                allure.attach(self.driver.get_screenshot_as_png(), name="Enter text in 'Other' field",
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
            'area_of_int': getattr(self, 'entered_area_of_int', None),
            'm_dig_spend': getattr(self, 'entered_m_dig_spend', None),
            'country': getattr(self, 'entered_country', None),
            'state': getattr(self, 'entered_state', None),
            'text_c': getattr(self, 'entered_text_c', None),
            'how_heard': getattr(self, 'entered_how_heard', None),
            'other': getattr(self, 'entered_text_other', None)
        }

    @allure.step("Get and save entered data")
    def get_and_save_entered_contact_data(self, filename, destination_path):
        entered_data = self.get_entered_data()

        with allure.step("Save entered data to Allure"):
            allure.attach(json.dumps(entered_data, indent=2), name="Entered Data",
                          attachment_type=allure.attachment_type.JSON)

        with open(filename, 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, destination_path)
        shutil.move(filename, destination_directory)
