from Pages.Forms.base_event_page import BaseEventPage
from Tests.locators.events_locators import EventFormLocators
from Tests.data.events_pages_data import Json_path
import allure

locators = EventFormLocators()

class EventsPages(BaseEventPage):

    # GENERAL FUNCTIONS
    @allure.step("Fill the form fields")
    def fill_form_fields(self):
        self.fill_form(
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

    @allure.step("Select the checkbox 'Privacy Policy'")
    def select_checkbox_step(self):
        self.select_checkbox(locators.privacy_policy)

    @allure.step("Select the checkbox 'Agree to contact me'")
    def select_checkbox_step_2(self):
        self.select_checkbox(locators.contact_me)

    def fill_report_form_and_save(self, json_filename, json_destination_path):
        self.fill_form_fields()
        self.select_checkbox_step()
        self.select_checkbox_step_2()
        self.get_and_save_entered_report_data(json_filename, json_destination_path)


    # FUNCTION FOR FILLING EACH REPORT FORM
    @allure.step("Fill the event form: Inspiring Dining: Media Leaders Roundtable")
    def fill_media_roundtable(self):
        self.fill_report_form_and_save('entered_data_media_roundtable_event.json', Json_path.media_roundtable_event)
