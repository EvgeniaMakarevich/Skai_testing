from Tests.locators.contact_page_locators import Fields_locators
from Pages.Forms.base_contact_page import ContactPage
from Tests.data.contact_page_data import Json_path
import json
import os
import shutil


class ContactPageMain(ContactPage):
    def fill_contact_main(self):
        self.fill_form(Fields_locators.name_input,
                       Fields_locators.email_input,
                       Fields_locators.lastname_input,
                       Fields_locators.company_input,
                       Fields_locators.job_title_input,
                       Fields_locators.area_of_int, Fields_locators.area_of_int_pot_options,
                       Fields_locators.selected_option_area_of_int,
                       Fields_locators.m_dig_spend, Fields_locators.m_dig_spend_options,
                       Fields_locators.selected_option_m_dig_spend,
                       Fields_locators.country, Fields_locators.country_option_usa,
                       Fields_locators.selected_option_country,
                       Fields_locators.state, Fields_locators.state_options, Fields_locators.selected_option_state,
                       Fields_locators.questions,
                       Fields_locators.how_heard, Fields_locators.how_heard_options,
                       Fields_locators.selected_option_how_heard)


        entered_data = self.get_entered_data()
        with open('entered_data_contact.json', 'w') as file:
            json.dump(entered_data, file)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        destination_directory = os.path.join(current_directory, Json_path.contact_page_main)
        shutil.move('entered_data_contact.json', destination_directory)












#
# class ContactPage(Base_page):
    # def fill_contact_form(self):
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.name_input)).send_keys('Test')
    #     self.entered_name = 'Test'
    #
    #     email = fake.email()
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.email_input)).send_keys(email)
    #     self.entered_email = email
    #
    #     last_name = fake.last_name()
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.lastname_input)).send_keys(last_name)
    #     self.entered_last_name = last_name
    #
    #
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.company_input)).send_keys('Dizzain')
    #     self.entered_company_name = 'Dizzain'
    #
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.job_title_input)).send_keys('QA')
    #     self.entered_job_title = 'QA'
    #
    #     area_of_int_option = self.select_random_option_from_dropdown(Fields_locators.area_of_int, Fields_locators.area_of_int_pot_options, Fields_locators.selected_option_area_of_int)
    #     self.entered_area_of_int = area_of_int_option
    #
    #
    #     m_dig_spend_option= self.select_random_option_from_dropdown(Fields_locators.m_dig_spend, Fields_locators.m_dig_spend_options, Fields_locators.selected_option_m_dig_spend)
    #     self.entered_m_dig_spend = m_dig_spend_option
    #
    #     country_option = self.select_exact_option(Fields_locators.country,Fields_locators.country_option_usa,Fields_locators.selected_option_country)
    #     self.entered_country = country_option
    #
    #
    #     state_option = self.select_random_option_from_dropdown(Fields_locators.state,
    #                                             Fields_locators.state_options, Fields_locators.selected_option_state)
    #     self.entered_state = state_option
    #
    #     text_c = fake.text()
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.questions)).send_keys(text_c)
    #     self.entered_text_c = text_c
    #
    #     how_heard_option = self.select_random_option_from_dropdown(Fields_locators.how_heard, Fields_locators.how_heard_options, Fields_locators.selected_option_how_heard)
    #     self.entered_how_heard = how_heard_option

    # def fill_form(self, name_locator, email_locator, last_name_locator, company_name_locator, job_title_locator,
    #               area_of_int_locator,area_of_int_options, area_of_int_soption, m_dig_spend_locator,m_dig_spend_options,
    #               m_dig_spend_soption, country_locator,country_option_usa, country_soptions, state_locator,state_options,
    #               state_soption, text_c_locator,how_heard_locator,how_heard_options, how_heard_soption):
    #
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(name_locator)).send_keys('Internal test')
    #     self.entered_name = 'Internal test'
    #
    #     email = fake.email()
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_locator)).send_keys(email)
    #     self.entered_email = email
    #
    #     last_name = fake.last_name()
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(last_name_locator)).send_keys('Test123')
    #     self.entered_last_name = 'Test123'
    #
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(company_name_locator)).send_keys('Dizzain')
    #     self.entered_company_name = 'Dizzain'
    #
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(job_title_locator)).send_keys('QA')
    #     self.entered_job_title = 'QA'
    #
    #     time.sleep(3)
    #
    #     area_of_int_option = self.select_random_option_from_dropdown(area_of_int_locator,area_of_int_options, area_of_int_soption)
    #     self.entered_area_of_int = area_of_int_option
    #
    #     m_dig_spend_option= self.select_random_option_from_dropdown(m_dig_spend_locator,m_dig_spend_options,m_dig_spend_soption)
    #     self.entered_m_dig_spend = m_dig_spend_option
    #
    #     country_option = self.select_exact_option(country_locator,country_option_usa, country_soptions)
    #     self.entered_country = country_option
    #
    #     state_option = self.select_random_option_from_dropdown(state_locator,state_options,state_soption)
    #     self.entered_state = state_option
    #
    #     text_c = fake.text()
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(text_c_locator)).send_keys(text_c)
    #     self.entered_text_c = text_c
    #
    #     how_heard_option = self.select_random_option_from_dropdown(how_heard_locator,how_heard_options, how_heard_soption)
    #     self.entered_how_heard = how_heard_option
    #
    # def get_entered_data(self):
    #     return {
    #         'name': getattr(self, 'entered_name', None),
    #         'email': getattr(self, 'entered_email', None),
    #         'last_name': getattr(self, 'entered_last_name', None),
    #         'company_name': getattr(self,'entered_company_name', None),
    #         'job_title': getattr(self,'entered_job_title', None),
    #         'area_of_int': getattr(self, 'entered_area_of_int', None),
    #         'm_dig_spend': getattr(self, 'entered_m_dig_spend', None),
    #         'country': getattr(self, 'entered_country', None),
    #         'state': getattr(self, 'entered_state', None),
    #         'text_c': getattr(self,'entered_text_c',None),
    #         'how_heard': getattr(self,'entered_how_heard', None)
    #     }

    # def submit_contact_form(self):
    #     return self.submit_form(Button.button_contact_us)

    # def submit_form(self, submit_button_locator):
    #     return self.submit_form(submit_button_locator)



