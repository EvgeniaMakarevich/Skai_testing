from Tests.data.reports_pages_data import Urls
from Tests.locators.pardot_locators import Contact_pardot
from Pages.Pardot.reports_pages.base_reports_page import PardotBaseReport
from Tests.data.reports_pages_data import ReportsNames
import json
from Tests.data.reports_pages_data import Json_path
import os

# current_directory = os.path.dirname(os.path.abspath(__file__))
# json_path = os.path.join(current_directory, Json_path.ai_report_pardot)
# with open(json_path, 'r') as file:
#     contact_data_ai = json.load(file)


class PardotAi(PardotBaseReport):
    def compare_data_ai(self, driver):
        ai_report = PardotBaseReport(driver, Urls.pardot_ai_form_handler)
        contact_data_ai = ai_report.load_json_data_reports(Json_path.ai_report_pardot)
        ai_report.compare_data(contact_data_ai)
        ai_report.compare_page_url(Contact_pardot.page_url, Urls.ai_url)
        ai_report.compare_report_name(ReportsNames.ai)
