from Tests.locators.pardot_locators import Contact_pardot
from Tests.data.sem_pages_data import Urls
from Pages.Pardot.Base_pardot_contact import PardotBaseContact
import json
from Tests.data.sem_pages_data import Json_path
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, Json_path.paid_search_pardot)
with open(json_path, 'r') as file:
    contact_data_paid_search = json.load(file)


class PardotPaidSearch(PardotBaseContact):
    def compare_data_paid_search(self, driver):
        paid_search = PardotBaseContact(driver, Contact_pardot.url_contact)
        paid_search.compare_data(contact_data_paid_search)
        paid_search.compare_page_url(Urls.paid_search_url)

