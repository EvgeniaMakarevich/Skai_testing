from Tests.locators.pardot_locators import Contact_pardot
from Tests.data.sem_pages_data import Urls
from Pages.Pardot.Base_pardot_contact import PardotBaseContact
import json
from Tests.data.sem_pages_data import Json_path
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, Json_path.paid_social_pardot)
with open(json_path, 'r') as file:
    contact_data_paid_social = json.load(file)


class PardotPaidSocial(PardotBaseContact):
    def compare_data_paid_social(self, driver):
        paid_social = PardotBaseContact(driver, Contact_pardot.url_contact)
        paid_social.compare_data(contact_data_paid_social)
        paid_social.compare_page_url(Urls.paid_social_url)
