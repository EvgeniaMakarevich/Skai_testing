from Tests.locators.contact_page_locators import Fields_locators
from Pages.Forms.base_contact_page import ContactPage
from Tests.data.contact_page_data import Json_path
import time
import allure


class ContactPageMain(ContactPage):
    def fill_contact_main(self, driver):

        with allure.step('Scroll to the form'):
            self.scroll_to_element(Fields_locators.contact_form)
            time.sleep(3)

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
                       Fields_locators.how_heard, Fields_locators.how_heard_option_other,
                       Fields_locators.selected_option_how_heard, Fields_locators.how_heard_field_other)

        self.get_and_save_entered_contact_data('entered_data_contact.json', Json_path.contact_page_main)