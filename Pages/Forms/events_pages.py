from Pages.Forms.base_event_page import BaseEventPage
from Tests.locators.events_locators import EventFormLocators
from Tests.data.events_pages_data import Json_path
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

locators = EventFormLocators()

class EventsPages(BaseEventPage):

    # GENERAL FUNCTIONS
    @allure.step("Fill the form fields")
    def fill_form_fields_1(self):
        self.fill_form_1(
            locators.first_name,
            locators.last_name,
            locators.email,
            locators.phone,
            locators.company,
            locators.job_title,
            locators.country,locators.country_option_usa, locators.selected_option_country,
            locators.state, locators.state_options,locators.selected_option_state,
            locators.dietary_req
        )

    @allure.step("Fill the form fields")
    def fill_form_fields_2(self):
        self.fill_form_2(
            locators.first_name,
            locators.last_name,
            locators.email,
            locators.company,
            locators.job_title,
            locators.what_interested_in, locators.what_interested_in_options, locators.selected_option_what_interested_in,
            locators.what_to_discuss
        )


    @allure.step("Select the checkbox 'Privacy Policy'")
    def select_checkbox_step(self):
        try:
            with allure.step("Selecting the checkbox 'Privacy Policy'"):
                self.select_checkbox(locators.privacy_policy)
                allure.attach(self.driver.get_screenshot_as_png(), name="Selecting the checkbox 'Privacy Policy'",
                              attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error selecting checkbox",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("Select the checkbox 'Agree to contact me'")
    def select_checkbox_step_2(self):
        # self.select_checkbox(locators.contact_me)
        try:
            with allure.step("Selecting the checkbox 'Agree to contact me'"):
                self.select_checkbox(locators.contact_me)
                allure.attach(self.driver.get_screenshot_as_png(), name="Selecting the checkbox 'Agree to contact me'",
                              attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error selecting checkbox",
                          attachment_type=allure.attachment_type.PNG)
            raise e


    def fill_event_form_and_save_1(self, json_filename, json_destination_path):
        self.fill_form_fields_1()
        self.select_checkbox_step()
        self.select_checkbox_step_2()
        self.get_and_save_entered_report_data_1(json_filename, json_destination_path)


    def fill_event_form_and_save_2(self, json_filename, json_destination_path):
        self.fill_form_fields_2()
        self.select_checkbox_step()
        self.select_checkbox_step_2()
        self.get_and_save_entered_report_data_2(json_filename, json_destination_path)


    # FUNCTION FOR FILLING EACH REPORT FORM
    @allure.step("Fill the event form: Inspiring Dining: Media Leaders Roundtable")
    def fill_media_roundtable(self):
        self.fill_event_form_and_save_1('entered_data_media_roundtable_event.json', Json_path.media_roundtable_event)

    @allure.step("eTail Happy Hour with iDerive & Skai")
    def fill_iDerive(self):
        self.fill_event_form_and_save_1('entered_data_iderive_event.json', Json_path.iderive_event)

    @allure.step("Meet Skai at Shoptalk US")
    def fill_shoptalk(self):
        self.scroll_to_element(locators.form_locator)
        time.sleep(3)

        self.fill_event_form_and_save_2('entered_data_shoptalk_event.json', Json_path.shoptalk_event)
