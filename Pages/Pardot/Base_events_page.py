import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Base_page import Base_page
from Tests.locators.pardot_locators import Contact_pardot, Form_handler
import allure
import time


class PardotBaseEvent(Base_page):
    def compare_data(self, contact_data):
        self.open()

        leads = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located((By.XPATH, Form_handler.all_leads)))

        self.scroll_to_element(Form_handler.all_leads)
        self.driver.execute_script("window.scrollBy(0, -200);")
        time.sleep(3)

        entered_name = f"{contact_data['name']} {contact_data['last_name']}"

        try:
            for lead in leads:
                if lead.text == entered_name:
                    lead.click()
                    break
        except Exception as e:
            print(f"Error during lead click: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Error during lead click",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Error message during lead click",
                          attachment_type=allure.attachment_type.TEXT)
            raise e

        name_pardot = self.driver.find_element(By.XPATH, Contact_pardot.name_field).text.strip()
        expected_name = f"{contact_data['name']} {contact_data['last_name']}"

        email_pardot = self.driver.find_element(By.XPATH, Contact_pardot.email_field).text.strip()
        expected_email = contact_data['email']

        company_pardot = self.driver.find_element(By.XPATH, Contact_pardot.company_field).text.strip()
        expected_company = contact_data['company_name']

        job_title_pardot = self.driver.find_element(By.XPATH, Contact_pardot.job_title_field).text.strip()
        expected_job_title = contact_data['job_title']

        phone_pardot = self.driver.find_element(By.XPATH, Contact_pardot.phone_field).text.strip()
        expected_phone = contact_data['phone']

        country_pardot = self.driver.find_element(By.XPATH, Contact_pardot.country_field).text.strip()
        expected_country = contact_data['country']

        state_pardot = self.driver.find_element(By.XPATH, Contact_pardot.state_field).text.strip()
        expected_state = contact_data['state']

        dietary_req = self.driver.find_element(By.XPATH, Contact_pardot.dietary_req_field).text.strip()
        expected_dietary_req = contact_data['dietary_req'].replace("\n", " ")

        # gdpr_pardot = self.driver.find_element(By.XPATH, Contact_pardot.gdpr).text.strip()
        # expected_gdpr_1 = 'Opt-In'
        # expected_gdpr_2 = 'Opt-In gdpr-field'

        if 'Undeliverable' in email_pardot:
            email_pardot = email_pardot.replace('Undeliverable', '').strip()

        if 'Mailable' in email_pardot:
            email_pardot = email_pardot.replace('Mailable', '').strip()

        asserts = [
            (name_pardot, expected_name, "Name_pardot"),
            (email_pardot, expected_email, "Email_pardot"),
            (company_pardot, expected_company, "Company_pardot"),
            (job_title_pardot, expected_job_title, "Job_title_pardot"),
            (phone_pardot, expected_phone, "Phone_pardot"),
            (country_pardot, expected_country, "Country_pardot"),
            (state_pardot, expected_state, "State_pardot"),
            (dietary_req.replace(" ", ""), expected_dietary_req.replace(" ", ""), "Dietary_req_pardot")
            # (gdpr_pardot, expected_gdpr_1 or expected_gdpr_2, "Gdpr_pardot")
        ]

        asserts_results = {}

        for value, expected, label in asserts:
            assert_result = {}
            try:
                assert value in expected, f"{label}:{value}, expected: {expected}"
                assert_result = {"status": "Passed", "message": f"Pardot {label}: {value} === Expected {label}: {expected}"}

            except AssertionError as e:
                print(f"Assertion error in {label}: {e}")
                assert_result = {"status": "Failed", "message": f"Pardot{label}: {value} !=== Expected {label}: {expected}"}

                allure.attach(self.driver.get_screenshot_as_png(), name=f"Assertion error in {label}",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(e), name=f"Assertion error message in {label}",
                              attachment_type=allure.attachment_type.TEXT)
            finally:
                asserts_results[label] = assert_result

        allure.attach(json.dumps(asserts_results, indent=2), name='All Asserts Results',
                      attachment_type=allure.attachment_type.JSON)

    @allure.step("Load JSON data")
    def load_json_data_events(self, json_path):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_directory, json_path)

        with open(full_path, 'r') as file:
            json_data = json.load(file)

        allure.attach(json.dumps(json_data, indent=2), name='Loaded Entered Data from form',
                      attachment_type=allure.attachment_type.JSON)

        return json_data

