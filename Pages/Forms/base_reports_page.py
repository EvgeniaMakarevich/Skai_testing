from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from Pages.Base_page import Base_page

fake = Faker()


class BaseReportPage(Base_page):
    def fill_form(self, name_locator, email_locator, last_name_locator, company_name_locator, job_title_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(name_locator)).send_keys('Internal test')
        self.entered_name = 'Internal test'

        email = fake.email()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_locator)).send_keys(email)
        self.entered_email = email

        last_name = fake.last_name()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(last_name_locator)).send_keys(last_name)
        self.entered_last_name = last_name

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(company_name_locator)).send_keys('Dizzain')
        self.entered_company_name = 'Dizzain'

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(job_title_locator)).send_keys('QA')
        self.entered_job_title = 'QA'


    def get_entered_data(self):
        return {
            'name': getattr(self, 'entered_name', None),
            'email': getattr(self, 'entered_email', None),
            'last_name': getattr(self, 'entered_last_name', None),
            'company_name': getattr(self, 'entered_company_name', None),
            'job_title': getattr(self, 'entered_job_title', None),
        }
