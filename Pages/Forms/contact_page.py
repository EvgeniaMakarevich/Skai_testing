from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from Pages.Base_page import Base_page
from Tests.locators.contact_page_locators import Fields_locators, Button
import time


fake = Faker()


class ContactPage(Base_page):
    def fill_contact_form(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.name_input)).send_keys('Test')
        self.entered_name = 'Test'

        email = fake.email()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.email_input)).send_keys(email)
        self.entered_email = email

        last_name = fake.last_name()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.lastname_input)).send_keys(last_name)
        self.entered_last_name = last_name


        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.company_input)).send_keys('Dizzain')
        self.entered_company_name = 'Dizzain'

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.job_title_input)).send_keys('QA')
        self.entered_job_title = 'QA'

        area_of_int_option = self.select_random_option_from_dropdown(Fields_locators.area_of_int, Fields_locators.area_of_int_pot_options, Fields_locators.selected_option_area_of_int)
        self.entered_area_of_int = area_of_int_option


        m_dig_spend_option= self.select_random_option_from_dropdown(Fields_locators.m_dig_spend, Fields_locators.m_dig_spend_options, Fields_locators.selected_option_m_dig_spend)
        self.entered_m_dig_spend = m_dig_spend_option

        country_option = self.select_exact_option(Fields_locators.country,Fields_locators.country_option_usa,Fields_locators.selected_option_country)
        self.entered_country = country_option


        state_option = self.select_random_option_from_dropdown(Fields_locators.state,
                                                Fields_locators.state_options, Fields_locators.selected_option_state)
        self.entered_state = state_option

        text_c = fake.text()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.questions)).send_keys(text_c)
        self.entered_text_c = text_c

        how_heard_option = self.select_random_option_from_dropdown(Fields_locators.how_heard, Fields_locators.how_heard_options, Fields_locators.selected_option_how_heard)
        self.entered_how_heard = how_heard_option

    def get_entered_data(self):
        return {
            'name': getattr(self, 'entered_name', None),
            'email': getattr(self, 'entered_email', None),
            'last_name': getattr(self, 'entered_last_name', None),
            'company_name': getattr(self,'entered_company_name', None),
            'job_title': getattr(self,'entered_job_title', None),
            'area_of_int': getattr(self, 'entered_area_of_int', None),
            'm_dig_spend': getattr(self, 'entered_m_dig_spend', None),
            'country': getattr(self, 'entered_country', None),
            'state': getattr(self, 'entered_state', None),
            'text_c': getattr(self,'entered_text_c',None),
            'how_heard': getattr(self,'entered_how_heard', None)
        }

    def submit_contact_form(self):
        return self.submit_form(Button.button_contact_us)


