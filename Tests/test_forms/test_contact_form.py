from Pages.Forms.contact_page import ContactPage
from Tests.data.Contact_page_data import Url,Json_path
from Tests.locators.contact_page_locators import Fields_locators, Button
from conftest import driver
import json


def test_submit_contact_form(driver):
    contact_page = ContactPage(driver, Fields_locators.url)
    contact_page.open()
    contact_page.borlabs_banner_close()
    contact_page.fill_form(Fields_locators.name_input,
                           Fields_locators.email_input,
                           Fields_locators.lastname_input,
                           Fields_locators.company_input,
                           Fields_locators.job_title_input,
                           Fields_locators.area_of_int,Fields_locators.area_of_int_pot_options, Fields_locators.selected_option_area_of_int,
                           Fields_locators.m_dig_spend, Fields_locators.m_dig_spend_options,Fields_locators.selected_option_m_dig_spend,
                           Fields_locators.country,Fields_locators.country_option_usa, Fields_locators.selected_option_country,
                           Fields_locators.state,Fields_locators.state_options, Fields_locators.selected_option_state,
                           Fields_locators.questions,
                           Fields_locators.how_heard, Fields_locators.how_heard_options,Fields_locators.selected_option_how_heard)

    entered_data = contact_page.get_entered_data()

    with open(Json_path.contact_page, 'w') as file:
        json.dump(entered_data, file)

    contact_page.submit_form(Button.button_contact_us)
    assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'
    return contact_page.get_entered_data()
