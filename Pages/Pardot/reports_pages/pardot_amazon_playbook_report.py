from Tests.data.reports_pages_data import Urls
from Tests.locators.pardot_locators import Contact_pardot
from Pages.Pardot.reports_pages.base_reports_page import PardotBaseReport
from Tests.data.reports_pages_data import ReportsNames
import json
from Tests.data.reports_pages_data import Json_path
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, Json_path.amazon_playbook_report_pardot)
with open(json_path, 'r') as file:
    contact_data_amazon_playbook = json.load(file)


class PardotAmazon(PardotBaseReport):
    def compare_data_amazon_playbook(self, driver):
        amazon_playbook = PardotBaseReport(driver, Urls.pardot_amazon_form_handler)
        amazon_playbook.compare_data(contact_data_amazon_playbook)
        amazon_playbook.compare_page_url(Contact_pardot.page_url, Urls.amazon_url)
        amazon_playbook.compare_report_name(ReportsNames.amazon_playbook)