from Tests.data.reports_pages_data import Urls
from Tests.locators.pardot_locators import Contact_pardot
from Pages.Pardot.Base_reports_page import PardotBaseReport
from Tests.data.reports_pages_data import ReportsNames
import allure
from Tests.data.reports_pages_data import Json_path

class ReportPagesPardot(PardotBaseReport):

    @allure.step("Compare data QTR_2024_4 report")
    def compare_data_qtr2023_4(self, driver):
        qtr_2023_4_report = PardotBaseReport(driver, Urls.pardot_qtr2023_4_form_handler)
        contact_data_qtr_2023_4 = qtr_2023_4_report.load_json_data_reports(Json_path.qtr2023_4_report_pardot)
        qtr_2023_4_report.compare_data(contact_data_qtr_2023_4)
        # qtr_2023_4_report.compare_page_url(Contact_pardot.page_url, Urls.ai_url)
        # qtr_2023_4_report.compare_report_name(ReportsNames.ai)

    @allure.step("Compare data QTR_2024_3 report")
    def compare_data_qtr2023_3(self, driver):
        qtr_2023_3_report = PardotBaseReport(driver, Urls.pardot_qtr2023_3_form_handler)
        contact_data_qtr_2023_3 = qtr_2023_3_report.load_json_data_reports(Json_path.qtr2023_3_report_pardot)
        qtr_2023_3_report.compare_data(contact_data_qtr_2023_3)
        # qtr_2023_4_report.compare_page_url(Contact_pardot.page_url, Urls.ai_url)
        # qtr_2023_4_report.compare_report_name(ReportsNames.ai)

    @allure.step("Compare data QTR_2024_2 report")
    def compare_data_qtr2023_2(self, driver):
        qtr_2023_2_report = PardotBaseReport(driver, Urls.pardot_qtr2023_2_form_handler)
        contact_data_qtr_2023_2 = qtr_2023_2_report.load_json_data_reports(Json_path.qtr2023_2_report_pardot)
        qtr_2023_2_report.compare_data(contact_data_qtr_2023_2)
        # qtr_2023_4_report.compare_page_url(Contact_pardot.page_url, Urls.ai_url)
        # qtr_2023_4_report.compare_report_name(ReportsNames.ai)

    @allure.step("Compare data AI report")
    def compare_data_ai(self, driver):
        ai_report = PardotBaseReport(driver, Urls.pardot_ai_form_handler)
        contact_data_ai = ai_report.load_json_data_reports(Json_path.ai_report_pardot)
        ai_report.compare_data(contact_data_ai)
        ai_report.compare_page_url(Contact_pardot.page_url, Urls.ai_url)
        ai_report.compare_report_name(ReportsNames.ai)

    @allure.step("Compare Hidden cost data report")
    def compare_data_hidden_cost(self, driver):
        hidden_cost = PardotBaseReport(driver, Urls.pardot_hidden_cost_handler)
        contact_data_hidden_cost = hidden_cost.load_json_data_reports(Json_path.hidden_cost_report_pardot)
        hidden_cost.compare_data(contact_data_hidden_cost)
        hidden_cost.compare_page_url(Contact_pardot.page_url, Urls.hidden_cost_url)
        hidden_cost.compare_report_name(ReportsNames.hidden_cost)

    @allure.step("Compare Prima Day data report")
    def compare_data_prime_day(self, driver):
        prime_day = PardotBaseReport(driver, Urls.pardot_prime_day_form_handler)
        contact_data_prime_day = prime_day.load_json_data_reports(Json_path.prime_day_report_pardot)
        prime_day.compare_data(contact_data_prime_day)
        prime_day.compare_page_url(Contact_pardot.page_url, Urls.prime_day_url)
        prime_day.compare_report_name(ReportsNames.prime_day)

    @allure.step("Compare Apple ads data report")
    def compare_data_apple_ads(self, driver):
        apple_ads = PardotBaseReport(driver, Urls.pardot_apple_ads_form_handler)
        contact_data_apple_ads = apple_ads.load_json_data_reports(Json_path.apple_ads_report_pardot)
        apple_ads.compare_data(contact_data_apple_ads)
        apple_ads.compare_page_url(Contact_pardot.page_url, Urls.apple_ads_url)
        apple_ads.compare_report_name(ReportsNames.apple_ads)

    @allure.step("Compare AMC playbook data report")
    def compare_data_amazon_playbook(self, driver):
        amazon_playbook = PardotBaseReport(driver, Urls.pardot_amazon_form_handler)
        contact_data_amazon_playbook = amazon_playbook.load_json_data_reports(Json_path.amazon_playbook_report_pardot)
        amazon_playbook.compare_data(contact_data_amazon_playbook)
        amazon_playbook.compare_page_url(Contact_pardot.page_url, Urls.amazon_url)
        amazon_playbook.compare_report_name(ReportsNames.amazon_playbook)