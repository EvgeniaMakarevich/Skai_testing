from Pages.Forms.base_contact_page import ContactPage
from Tests.locators.contact_page_locators import Fields_locators
from Tests.data.sem_pages_data import Json_path
from Tests.locators.sem_pages_locators import Checkbox
import time
import allure

class SemPages(ContactPage):

    # GENERAL FUNCTIONS
    @allure.step("Scroll to the form")
    def scroll_to_form(self):
        self.scroll_to_element(Fields_locators.contact_form)
        time.sleep(2)

    @allure.step("Fill the form fields")
    def fill_sem_page(self):
        self.fill_form(
            Fields_locators.name_input,
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
            Fields_locators.selected_option_how_heard, Fields_locators.how_heard_field_other
        )

    @allure.step("Select the checkbox")
    def select_checkbox_step(self):
        self.select_checkbox(Checkbox.checkbox)


    # FUNCTIONS FOR FILLING EACH SEM FORM
    def fill_sem_page_and_save(self,json_filename, json_destination_path):
        self.scroll_to_form()
        self.fill_sem_page()
        self.select_checkbox_step()
        self.get_and_save_entered_contact_data(json_filename, json_destination_path)

    @allure.step("Fill SEM page: Paid Social")
    def fill_sem_page_paid_social(self):
        self.fill_sem_page_and_save('entered_data_paid_social.json', Json_path.paid_social)

    @allure.step("Fill SEM page: Paid Search")
    def fill_sem_page_paid_search(self):
        self.fill_sem_page_and_save('entered_data_paid_search.json', Json_path.paid_search)

    @allure.step("Fill SEM page: Retail Solution")
    def fill_sem_page_retail_solution(self):
        self.fill_sem_page_and_save('entered_data_retail_solution.json', Json_path.retail_solution)

    @allure.step("Fill SEM page: Amazon Ads")
    def fill_sem_page_amazon_ads(self):
        self.fill_sem_page_and_save('entered_data_amazon_ads.json', Json_path.amazon_ads)





