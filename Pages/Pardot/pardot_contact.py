from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Base_page import Base_page
import time
from Tests.locators.pardot_locators import Contact_pardot
from Pages.Forms.contact_page import ContactPage
import json

with open('/Pages/Pardot/json_data/entered_data_contact.json', 'r') as file:
    contact_data = json.load(file)


class Pardot(Base_page):
    def contact_page(self):
        contact_page = ContactPage(self.driver, Contact_pardot.url_contact)
        self.open()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Contact_pardot.last_lead_link))).click()

        name_pardot = self.driver.find_element(By.XPATH, Contact_pardot.name_field).text.strip()
        expected_name = f"{contact_data['name']} {contact_data['last_name']}"

        email_pardot = self.driver.find_element(By.XPATH, Contact_pardot.email_field).text.strip()
        expected_email = contact_data['email']

        company_pardot = self.driver.find_element(By.XPATH, Contact_pardot.company_field).text.strip()
        expected_company = contact_data['company_name']

        job_title_pardot = self.driver.find_element(By.XPATH, Contact_pardot.job_title_field).text.strip()
        expected_job_title = contact_data['job_title']

        country_pardot = self.driver.find_element(By.XPATH, Contact_pardot.company_field).text.strip()
        expected_country = contact_data['country']

        state_pardot = self.driver.find_element(By.XPATH, Contact_pardot.state_field).text.strip()
        expected_state = contact_data['state']


        assert name_pardot == expected_name, f"Name_pardot:{name_pardot},expected_name: {expected_name}"
        assert email_pardot == expected_email, f"Email_pardot:{email_pardot},expected_email: {expected_email}"
        assert company_pardot == expected_company, f"Company_pardot:{company_pardot},expected_company: {expected_company}"
        assert job_title_pardot == expected_job_title, f"Job_title_pardot:{job_title_pardot},expected_job_title: {expected_job_title}"
        assert country_pardot == expected_country, f"Country_pardot:{country_pardot},expected_country: {expected_country}"
        assert state_pardot == expected_state, f"State_pardot:{state_pardot}, expected_state: {expected_state}"



