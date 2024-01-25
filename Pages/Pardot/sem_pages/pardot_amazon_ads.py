from Tests.locators.pardot_locators import Contact_pardot
from Tests.data.sem_pages_data import Urls
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
        amazon_ads = PardotBaseContact(driver, Contact_pardot.url_contact)
        # contact_data_amazon_ads = LoadJsonSem.load_json_data_sem(Json_path.amazon_ads_pardot)
        amazon_ads.compare_data(contact_data_amazon_ads)
        amazon_ads.compare_page_url(Contact_pardot.page_url, Urls.amazon_ads_url)
