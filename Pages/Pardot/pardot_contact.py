from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Base_page import Base_page
from Tests.locators.pardot_locators import Contact_pardot,Form_handler
from Pages.Forms.contact_page import ContactPage
import json
from Tests.data.Contact_page_data import Json_path

with open(Json_path.contact_page, 'r') as file:
    contact_data = json.load(file)

# f"{contact_data['name']} {contact_data['last_name']}
class Pardot(Base_page):
    # def contact_page(self):
    #     contact_page = ContactPage(self.driver, Contact_pardot.url_contact)
    #     self.open()
    #
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, Contact_pardot.last_lead_link))).click()
    #
    #     name_pardot = self.driver.find_element(By.XPATH, Contact_pardot.name_field).text.strip()
    #     expected_name = f"{contact_data['name']} {contact_data['last_name']}"
    #
    #     email_pardot = self.driver.find_element(By.XPATH, Contact_pardot.email_field).text.strip()
    #     expected_email = contact_data['email']
    #
    #     company_pardot = self.driver.find_element(By.XPATH, Contact_pardot.company_field).text.strip()
    #     expected_company = contact_data['company_name']
    #
    #     job_title_pardot = self.driver.find_element(By.XPATH, Contact_pardot.job_title_field).text.strip()
    #     expected_job_title = contact_data['job_title']
    #
    #     country_pardot = self.driver.find_element(By.XPATH, Contact_pardot.company_field).text.strip()
    #     expected_country = contact_data['country']
    #
    #     state_pardot = self.driver.find_element(By.XPATH, Contact_pardot.state_field).text.strip()
    #     expected_state = contact_data['state']
    #
    #     channels_pardot = self.driver.find_element(By.XPATH, Contact_pardot.channels).text.strip()
    #     expected_channels = contact_data['area_of_int']
    #
    #     comment_pardot = self.driver.find_element(By.XPATH, Contact_pardot.comment).text.strip()
    #     expected_comment = contact_data['text_c']
    #
    #     how_heard_pardot = self.driver.find_element(By.XPATH, Contact_pardot.how_heard).text.strip()
    #     expected_how_heard = contact_data['how_heard']
    #
    #     m_dig_spend_pardot = self.driver.find_element(By.XPATH, Contact_pardot.m_dig_spend).text.strip()
    #     expected_m_dig_spend = contact_data['m_dig_spend']
    #
    #     assert name_pardot == expected_name, f"Name_pardot:{name_pardot},expected_name: {expected_name}"
    #     assert email_pardot == expected_email, f"Email_pardot:{email_pardot},expected_email: {expected_email}"
    #     assert company_pardot == expected_company, f"Company_pardot:{company_pardot},expected_company: {expected_company}"
    #     assert job_title_pardot == expected_job_title, f"Job_title_pardot:{job_title_pardot},expected_job_title: {expected_job_title}"
    #     assert country_pardot == expected_country, f"Country_pardot:{country_pardot},expected_country: {expected_country}"
    #     assert state_pardot == expected_state, f"State_pardot:{state_pardot}, expected_state: {expected_state}"
    #     assert channels_pardot == expected_channels, f"Channels_pardot:{channels_pardot}, expected_channels: {expected_channels}"
    #     assert comment_pardot == expected_comment, f"Comment_pardot:{comment_pardot}, expected_comment: {expected_comment}"
    #     assert how_heard_pardot == expected_how_heard, f"How_heard_pardot:{how_heard_pardot}, expected_how_heard: {expected_how_heard}"
    #     assert m_dig_spend_pardot == expected_m_dig_spend, f"M_dig_spend_pardot:{m_dig_spend_pardot}, expected_m_dig_spend: {expected_m_dig_spend}"

        def contact_page(self):
            contact_page = ContactPage(self.driver, Contact_pardot.url_contact)
            self.open()

            leads = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, Form_handler.all_leads)))

            # leads_names = [x.text for x in leads]
            entered_name = f"{contact_data['name']} {contact_data['last_name']}"

            for lead in leads:
                if lead.text == entered_name:
                    lead.click()
                    break

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

            channels_pardot = self.driver.find_element(By.XPATH, Contact_pardot.channels).text.strip()
            expected_channels = contact_data['area_of_int']

            comment_pardot = self.driver.find_element(By.XPATH, Contact_pardot.comment).text.strip()
            expected_comment = contact_data['text_c']

            how_heard_pardot = self.driver.find_element(By.XPATH, Contact_pardot.how_heard).text.strip()
            expected_how_heard = contact_data['how_heard']

            m_dig_spend_pardot = self.driver.find_element(By.XPATH, Contact_pardot.m_dig_spend).text.strip()
            expected_m_dig_spend = contact_data['m_dig_spend']

            assert name_pardot == expected_name, f"Name_pardot:{name_pardot},expected_name: {expected_name}"
            assert email_pardot == expected_email, f"Email_pardot:{email_pardot},expected_email: {expected_email}"
            assert company_pardot == expected_company, f"Company_pardot:{company_pardot},expected_company: {expected_company}"
            assert job_title_pardot == expected_job_title, f"Job_title_pardot:{job_title_pardot},expected_job_title: {expected_job_title}"
            assert country_pardot == expected_country, f"Country_pardot:{country_pardot},expected_country: {expected_country}"
            assert state_pardot == expected_state, f"State_pardot:{state_pardot}, expected_state: {expected_state}"
            assert channels_pardot == expected_channels, f"Channels_pardot:{channels_pardot}, expected_channels: {expected_channels}"
            assert comment_pardot == expected_comment, f"Comment_pardot:{comment_pardot}, expected_comment: {expected_comment}"
            assert how_heard_pardot == expected_how_heard, f"How_heard_pardot:{how_heard_pardot}, expected_how_heard: {expected_how_heard}"
            assert m_dig_spend_pardot == expected_m_dig_spend, f"M_dig_spend_pardot:{m_dig_spend_pardot}, expected_m_dig_spend: {expected_m_dig_spend}"
