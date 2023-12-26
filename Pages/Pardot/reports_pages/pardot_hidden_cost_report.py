from Tests.data.reports_pages_data import Urls
from Tests.locators.pardot_locators import Contact_pardot
from Pages.Pardot.reports_pages.base_reports_page import PardotBaseReport
import json
from Tests.data.reports_pages_data import Json_path
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, Json_path.hidden_cost_report_pardot)
with open(json_path, 'r') as file:
    contact_data_hidden_cost = json.load(file)


class PardotHiddenCost(PardotBaseReport):
    def compare_data_hidden_cost(self, driver):
        hidden_cost = PardotBaseReport(driver, Urls.pardot_hidden_cost_handler)
        hidden_cost.compare_data(contact_data_hidden_cost)
        hidden_cost.compare_page_url(Contact_pardot.page_url, Urls.hidden_cost_url)
