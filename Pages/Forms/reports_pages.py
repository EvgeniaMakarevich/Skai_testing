from Pages.Forms.base_reports_page import BaseReportPage
from Tests.locators.contact_page_locators import Fields_locators
from Tests.data.reports_pages_data import Json_path
from Tests.locators.sem_pages_locators import Checkbox
import time
import allure


class ReportsPages(BaseReportPage):

    #GENERAL FUNCTIONS
    @allure.step("Scroll to the form")
    def scroll_to_form(self):
        self.scroll_to_element(Fields_locators.contact_form)
        time.sleep(2)

    @allure.step("Fill the form fields")
    def fill_form_fields(self):
        self.fill_form(
            Fields_locators.name_input,
            Fields_locators.email_input,
            Fields_locators.lastname_input,
            Fields_locators.company_input,
            Fields_locators.job_title_input
        )

    @allure.step("Select the checkbox")
    def select_checkbox_step(self):
        self.select_checkbox(Checkbox.checkbox)



    #FUNCTIONS FOR FILLING EACH REPORT FORM
    @allure.step("Fill the report form: Hidden Cost.. ")
    def fill_hidden_cost(self):
        self.scroll_to_form()
        self.fill_form_fields()
        self.select_checkbox_step()
        self.get_and_save_entered_report_data('entered_data_hidden_cost_report', Json_path.hidden_cost_report)


    @allure.step("Fill the report form: The Next Big Thing: Where Generative AI’s..")
    def fill_ai(self):
        self.scroll_to_form()
        self.fill_form_fields()
        self.select_checkbox_step()
        self.get_and_save_entered_report_data('entered_data_ai_report', Json_path.ai_report)

    @allure.step("Fill the report form: Get Prepped for Prime Day 2023")
    def fill_prime_day(self):
        self.scroll_to_form()
        self.fill_form_fields()
        self.select_checkbox_step()
        self.get_and_save_entered_report_data('entered_data_prime_day_report', Json_path.prime_day_report)

    @allure.step("Fill the report form: Amazon Marketing Cloud Playbook")
    def fill_amazon_playbook(self):
        self.scroll_to_form()
        self.fill_form_fields()
        self.select_checkbox_step()
        self.get_and_save_entered_report_data('entered_data_amazon_playbook_report', Json_path.amazon_playbook_report)

    @allure.step("Fill the report form: Mastering Apple Search Ads")
    def fill_apple_ads(self):
        self.scroll_to_form()
        self.fill_form_fields()
        self.select_checkbox_step()
        self.get_and_save_entered_report_data('entered_data_apple_ads_report', Json_path.apple_ads_report)









    # def fill_hidden_cost(self, driver):
    #     self.scroll_to_element(Fields_locators.contact_form)
    #     time.sleep(2)
    #
    #     self.fill_form(Fields_locators.name_input,
    #                    Fields_locators.email_input,
    #                    Fields_locators.lastname_input,
    #                    Fields_locators.company_input,
    #                    Fields_locators.job_title_input)
    #
    #     self.select_checkbox(Checkbox.checkbox)
    #
    #     entered_data = self.get_entered_data()
    #     with open('entered_data_hidden_cost_report', 'w') as file:
    #         json.dump(entered_data, file)
    #
    #     current_directory = os.path.dirname(os.path.abspath(__file__))
    #     destination_directory = os.path.join(current_directory, Json_path.hidden_cost_report)
    #     shutil.move('entered_data_hidden_cost_report', destination_directory)


    # def fill_ai(self, driver):
    #     self.scroll_to_element(Fields_locators.contact_form)
    #     time.sleep(2)
    #
    #     self.fill_form(Fields_locators.name_input,
    #                    Fields_locators.email_input,
    #                    Fields_locators.lastname_input,
    #                    Fields_locators.company_input,
    #                    Fields_locators.job_title_input)
    #
    #     self.select_checkbox(Checkbox.checkbox)
    #
    #     entered_data = self.get_entered_data()
    #     with open('entered_data_ai_report', 'w') as file:
    #         json.dump(entered_data, file)
    #
    #     current_directory = os.path.dirname(os.path.abspath(__file__))
    #     destination_directory = os.path.join(current_directory, Json_path.ai_report)
    #     shutil.move('entered_data_ai_report', destination_directory)
    #
    # def fill_prime_day(self, driver):
    #     self.scroll_to_element(Fields_locators.contact_form)
    #     time.sleep(2)
    #
    #     self.fill_form(Fields_locators.name_input,
    #                    Fields_locators.email_input,
    #                    Fields_locators.lastname_input,
    #                    Fields_locators.company_input,
    #                    Fields_locators.job_title_input)
    #
    #     self.select_checkbox(Checkbox.checkbox)
    #
    #     entered_data = self.get_entered_data()
    #     with open('entered_data_prime_day_report', 'w') as file:
    #         json.dump(entered_data, file)
    #
    #     current_directory = os.path.dirname(os.path.abspath(__file__))
    #     destination_directory = os.path.join(current_directory, Json_path.prime_day_report)
    #     shutil.move('entered_data_prime_day_report', destination_directory)
    #
    #
    # def fill_amazon_playbook(self, driver):
    #     self.scroll_to_element(Fields_locators.contact_form)
    #     time.sleep(2)
    #
    #     self.fill_form(Fields_locators.name_input,
    #                    Fields_locators.email_input,
    #                    Fields_locators.lastname_input,
    #                    Fields_locators.company_input,
    #                    Fields_locators.job_title_input)
    #
    #     self.select_checkbox(Checkbox.checkbox)
    #
    #     entered_data = self.get_entered_data()
    #     with open('entered_data_amazon_playbook_report', 'w') as file:
    #         json.dump(entered_data, file)
    #
    #     current_directory = os.path.dirname(os.path.abspath(__file__))
    #     destination_directory = os.path.join(current_directory, Json_path.amazon_playbook_report)
    #     shutil.move('entered_data_amazon_playbook_report', destination_directory)
    #
    #
    # def fill_apple_ads(self, driver):
    #     self.scroll_to_element(Fields_locators.contact_form)
    #     time.sleep(2)
    #
    #     self.fill_form(Fields_locators.name_input,
    #                    Fields_locators.email_input,
    #                    Fields_locators.lastname_input,
    #                    Fields_locators.company_input,
    #                    Fields_locators.job_title_input)
    #
    #     self.select_checkbox(Checkbox.checkbox)
    #
    #     entered_data = self.get_entered_data()
    #     with open('entered_data_apple_ads_report', 'w') as file:
    #         json.dump(entered_data, file)
    #
    #     current_directory = os.path.dirname(os.path.abspath(__file__))
    #     destination_directory = os.path.join(current_directory, Json_path.apple_ads_report)
    #     shutil.move('entered_data_apple_ads_report', destination_directory)
