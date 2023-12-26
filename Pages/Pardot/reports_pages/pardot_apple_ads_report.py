from Tests.data.reports_pages_data import Urls
from Tests.locators.pardot_locators import Contact_pardot
from Pages.Pardot.reports_pages.base_reports_page import PardotBaseReport
import json
from Tests.data.reports_pages_data import Json_path
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, Json_path.apple_ads_report_pardot)
with open(json_path, 'r') as file:
    contact_data_apple_ads = json.load(file)


class PardotAppleAds(PardotBaseReport):
    def compare_data_apple_ads(self, driver):
        apple_ads = PardotBaseReport(driver, Urls.pardot_apple_ads_form_handler)
        apple_ads.compare_data(contact_data_apple_ads)
        apple_ads.compare_page_url(Contact_pardot.page_url, Urls.apple_ads_url)