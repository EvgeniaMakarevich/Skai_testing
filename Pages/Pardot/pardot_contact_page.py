from Tests.locators.pardot_locators import Contact_pardot
from Pages.Pardot.Base_pardot_contact import PardotBaseContact
import json
import os
from Tests.data.Contact_page_data import Json_path

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, Json_path.contact_page_main)
with open(json_path, 'r') as file:
    contact_data_main_contact = json.load(file)


class PardotContactPage(PardotBaseContact):
    def compare_data_contact_page(self, driver):
        contact_page = PardotBaseContact(driver, Contact_pardot.url_contact)
        contact_page.compare_data(contact_data_main_contact)




