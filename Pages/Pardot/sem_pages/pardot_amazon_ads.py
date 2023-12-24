from Tests.locators.pardot_locators import Contact_pardot
from Pages.Pardot.Base_pardot_contact import PardotBaseContact
import json
from Tests.data.sem_pages_data import Json_path
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, Json_path.amazon_ads_pardot)
with open(json_path, 'r') as file:
    contact_data_amazon_ads = json.load(file)


class PardotAmazonAds(PardotBaseContact):
    def compare_data_amazon_ads(self, driver):
        paid_social = PardotBaseContact(driver, Contact_pardot.url_contact)
        paid_social.compare_data(contact_data_amazon_ads)