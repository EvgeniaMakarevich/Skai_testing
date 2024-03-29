from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from Pages.Base_page import Base_page
import allure
import json
import os
import shutil

fake = Faker()


class BaseReportPage(Base_page):
    @allure.step('Fill report form')
    def fill_form(self, name_locator, email_locator, last_name_locator, company_name_locator, job_title_locator):
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
        }

    @allure.step("Get and save entered data")
    def get_and_save_entered_report_data(self, filename, destination_path):
        entered_data = self.get_entered_data()

        with allure.step("Save entered data to Allure"):
            allure.attach(json.dumps(entered_data, indent=2), name="Entered Data",
                          attachment_type=allure.attachment_type.JSON)

        with open(filename, 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, destination_path)
        shutil.move(filename, destination_directory)
