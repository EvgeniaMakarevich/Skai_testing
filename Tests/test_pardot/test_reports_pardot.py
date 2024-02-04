from Tests.data.reports_pages_data import Urls
from Pages.Pardot.reports_pages import ReportPagesPardot
import allure
import pytest


class TestReportsPages:
    @allure.tag("Compare Pardot data with entered Reports data")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('Form_handler_url,fill_method, title, description', [

        (Urls.pardot_qtr2023_4_form_handler, ReportPagesPardot.compare_data_qtr2023_4, "Q4 2023 Report",
         "Compare Pardot data with entered 'Q4 2023 Quarterly Digital Trends Report' data"),

        (Urls.pardot_qtr2023_3_form_handler, ReportPagesPardot.compare_data_qtr2023_3, "Q3 2023 Report",
         "Compare Pardot data with entered 'Q3 2023 Quarterly Digital Trends Report' data"),

        (Urls.pardot_qtr2023_2_form_handler, ReportPagesPardot.compare_data_qtr2023_2, "Q2 2023 Report",
         "Compare Pardot data with entered 'Q2 2023 Quarterly Digital Trends Report' data"),

        (Urls.pardot_ai_form_handler, ReportPagesPardot.compare_data_ai, "Generative AI Report",
         "Compare Pardot data with entered 'The Next Big Thing: Where Generative AI’s.. report' data"),

        (Urls.pardot_hidden_cost_handler, ReportPagesPardot.compare_data_hidden_cost, "Hidden Cost Report",
         "Compare Pardot data with entered 'Hidden Cost Report' data")

        # (Urls.pardot_prime_day_form_handler, ReportPagesPardot.compare_data_prime_day, "Prime Day 2023 Report",
        #  "Compare Pardot data with entered 'Prime Day 2023 Report' data"),

        # (Urls.pardot_amazon_form_handler, ReportPagesPardot.compare_data_amazon_playbook,
        #  "Amazon Marketing Cloud Playbook Report",
        #  "Compare Pardot data with entered 'Amazon Marketing Cloud Playbook Report' data"),
        #
        # (Urls.pardot_apple_ads_form_handler, ReportPagesPardot.compare_data_apple_ads, "Apple Search Ads Report",
        #  "Compare Pardot data with entered 'Apple Search Ads Report' data"),

    ])
    def test_compare_report_data(self, get_pardot, Form_handler_url, fill_method, title, description):
        allure.dynamic.title(title)
        allure.dynamic.description(description)
        driver = get_pardot
        report = ReportPagesPardot(driver, Form_handler_url)
        driver.set_window_size(1920, 1080)
        fill_method(report, driver)


