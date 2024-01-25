from Pages.Forms.base_reports_page import BaseReportPage
from Tests.locators.contact_page_locators import Fields_locators
from Tests.data.reports_pages_data import Json_path
from Tests.locators.sem_pages_locators import Checkbox
import time
import allure


class ReportsPages(BaseReportPage):

        # GENERAL FUNCTIONS
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

        def fill_report_form_and_save(self, json_filename, json_destination_path):
            self.scroll_to_form()
            self.fill_form_fields()
            self.select_checkbox_step()
            self.get_and_save_entered_report_data(json_filename, json_destination_path)

        # FUNCTION FOR FILLING EACH REPORT FORM

        @allure.step("Fill the report form: Q4 2023 Quarterly Digital Trends Report")
        def fill_qtr2023_4(self):
            self.fill_report_form_and_save('entered_data_qtr2023_4_report.json', Json_path.qtr2023_4_report)

        @allure.step("Fill the report form: Q2 2023 Quarterly Digital Trends Report")
        def fill_qtr2023_3(self):
            self.fill_report_form_and_save('entered_data_qtr2023_3_report.json', Json_path.qtr2023_3_report)

        @allure.step("Fill the report form: Q2 2023 Quarterly Digital Trends Report")
        def fill_qtr2023_2(self):
            self.fill_report_form_and_save('entered_data_qtr2023_2_report.json', Json_path.qtr2023_2_report)

        @allure.step("Fill the report form: Hidden Cost..")
        def fill_hidden_cost(self):
            self.fill_report_form_and_save('entered_data_hidden_cost_report.json', Json_path.hidden_cost_report)

        @allure.step("Fill the report form: The Next Big Thing: Where Generative AI’s..")
        def fill_ai(self):
            self.fill_report_form_and_save('entered_data_ai_report.json', Json_path.ai_report)


        # @allure.step("Fill the report form: Get Prepped for Prime Day 2023")
        # def fill_prime_day(self):
        #     self.fill_report_form_and_save('entered_data_prime_day_report.json', Json_path.prime_day_report)
        #
        # @allure.step("Fill the report form: Amazon Marketing Cloud Playbook")
        # def fill_amazon_playbook(self):
        #     self.fill_report_form_and_save('entered_data_amazon_playbook_report.json', Json_path.amazon_playbook_report)
        #
        # @allure.step("Fill the report form: Mastering Apple Search Ads")
        # def fill_apple_ads(self):
        #     self.fill_report_form_and_save('entered_data_apple_ads_report.json', Json_path.apple_ads_report)
