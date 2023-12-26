from Tests.data.reports_pages_data import Urls
from Tests.locators.pardot_locators import Contact_pardot
from Pages.Pardot.reports_pages.base_reports_page import PardotBaseReport
import json
from Tests.data.reports_pages_data import Json_path
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, Json_path.prime_day_report_pardot)
with open(json_path, 'r') as file:
    contact_data_prime_day = json.load(file)


class PardotPrimeDay(PardotBaseReport):
    def compare_data_prime_day(self, driver):
        prime_day = PardotBaseReport(driver, Urls.pardot_prime_day_form_handler)
        prime_day.compare_data(contact_data_prime_day)
        prime_day.compare_page_url(Contact_pardot.page_url, Urls.prime_day_url)
