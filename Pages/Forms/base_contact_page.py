from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from Pages.Base_page import Base_page
from selenium.webdriver.common.action_chains import ActionChains
import time

fake = Faker()


class ContactPage(Base_page):
    def fill_form(self, name_locator, email_locator, last_name_locator, company_name_locator, job_title_locator,
                  area_of_int_locator, area_of_int_options, area_of_int_soption, m_dig_spend_locator,
                  m_dig_spend_options,
                  m_dig_spend_soption, country_locator, country_option_usa, country_soptions, state_locator,
                  state_options,
                  state_soption, text_c_locator, how_heard_locator, how_heard_options, how_heard_soption,
                  other_field_locator):
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

        time.sleep(3)

        area_of_int_option = self.select_random_option_from_dropdown(area_of_int_locator, area_of_int_options,
                                                                     area_of_int_soption)
        self.entered_area_of_int = area_of_int_option

        m_dig_spend_option = self.select_random_option_from_dropdown(m_dig_spend_locator, m_dig_spend_options,
                                                                     m_dig_spend_soption)
        self.entered_m_dig_spend = m_dig_spend_option

        country_option = self.select_exact_option(country_locator, country_option_usa, country_soptions)
        self.entered_country = country_option

        state_option = self.select_random_option_from_dropdown(state_locator, state_options, state_soption)
        self.entered_state = state_option

        text_c = fake.text()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(text_c_locator)).send_keys(text_c)
        self.entered_text_c = text_c

        # how_heard_option = self.select_random_option_from_dropdown(how_heard_locator, how_heard_options,
        #                                                            how_heard_soption)
        # self.entered_how_heard = how_heard_option

        how_heard_option = self.select_exact_option(how_heard_locator, how_heard_options, how_heard_soption)
        self.entered_how_heard = how_heard_option

        text_other = fake.text()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(other_field_locator)).send_keys(text_other)
        self.entered_text_other = text_other

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






