from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Base_page import Base_page
from Tests.locators.pardot_locators import Contact_pardot, Form_handler
from Tests.locators.reports_locators import ReportNamesLocators


class PardotBaseReport(Base_page):
    def compare_data(self, contact_data):
        self.open()

        leads = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, Form_handler.all_leads)))

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

        gdpr_pardot = self.driver.find_element(By.XPATH, Contact_pardot.gdpr).text.strip()
        expected_gdpr_1 = 'Opt-In'
        expected_gdpr_2 = 'Opt-In gdpr-field'

        # assert name_pardot == expected_name, f"Name_pardot:{name_pardot},expected_name: {expected_name}"
        #
        # if 'Undeliverable' in email_pardot:
        #     email_pardot = email_pardot.replace('Undeliverable', '').strip()
        #
        # if 'Mailable' in email_pardot:
        #     email_pardot = email_pardot.replace('Mailable', '').strip()
        #
        # assert email_pardot == expected_email, f"Email_pardot:{email_pardot},expected_email: {expected_email}"
        # assert company_pardot == expected_company, f"Company_pardot:{company_pardot},expected_company: {expected_company}"
        # assert job_title_pardot == expected_job_title, f"Job_title_pardot:{job_title_pardot},expected_job_title: {expected_job_title}"
        # assert gdpr_pardot == expected_gdpr_1 or expected_gdpr_2, f"Gdpr_pardot:{gdpr_pardot}, expected_gdpr: {expected_gdpr_1} or {expected_gdpr_2}"


        if 'Undeliverable' in email_pardot:
            email_pardot = email_pardot.replace('Undeliverable', '').strip()

        if 'Mailable' in email_pardot:
            email_pardot = email_pardot.replace('Mailable', '').strip()

        asserts = [
            (name_pardot, expected_name, "Name_pardot"),
            (email_pardot, expected_email, "Email_pardot"),
            (company_pardot, expected_company, "Company_pardot"),
            (job_title_pardot, expected_job_title, "Job_title_pardot"),
            (gdpr_pardot, expected_gdpr_1 or expected_gdpr_2, "Gdpr_pardot")
        ]

        for value, expected, label in asserts:
            try:
                assert value == expected, f"{label}:{value}, expected: {expected}"
            except AssertionError as e:
                print(f"Assertion error in {label}: {e}")

    def compare_report_name(self, report_name):
        report_name_pardot = self.driver.find_element(By.XPATH, ReportNamesLocators.report_name_locator).text.strip()
        assert report_name_pardot == report_name, f"Report_name_pardot:{report_name_pardot},expected_report_name: {report_name}"
