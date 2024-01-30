from Pages.Forms.reports_pages import ReportsPages
from Tests.data.reports_pages_data import Urls, Resource_download_urls
from conftest import driver, options
from Tests.locators.contact_page_locators import Button
import allure
import pytest



class TestFillReportPages:
    @allure.tag("Report form")
    @allure.severity(allure.severity_level.CRITICAL)

    @pytest.mark.parametrize("report_url, fill_method, resource_url, title, description",
                             [("https://skai.io/reports-and-whitepapers/the-hidden-cost-of-advertising-point-solutions/", ReportsPages.fill_hidden_cost, Resource_download_urls.hidden_cost, "Hidden Cost Report", "Fill form of report 'The Hidden Cost of Advertising Point Solutions'"),
                              ("https://skai.io/reports-and-whitepapers/embracing-generative-ai/", ReportsPages.fill_ai, Resource_download_urls.ai, "Generative AI Report", "Fill form of report 'The Next Big Thing: Where Generative AI’s..'"),
                              ("https://skai.io/reports-and-whitepapers/q4-2023-quarterly-digital-trends-report/", ReportsPages.fill_qtr2023_4, ReportsPages.fill_hidden_cost, 'Q4 2023 Quarterly Trends Report',"Fill form of report 'Q4 2023 Quarterly Trends Report'"),
                              ("https://skai.io/reports-and-whitepapers/q3-2023-quarterly-digital-trends-report/", ReportsPages.fill_qtr2023_3, ReportsPages.fill_hidden_cost,'Q3 2023 Quarterly Trends Report',"Fill form of report 'Q3 2023 Quarterly Trends Report'"),
                              ("https://skai.io/reports-and-whitepapers/q2-2023-quarterly-digital-trends-report/", ReportsPages.fill_qtr2023_2, ReportsPages.fill_hidden_cost, 'Q2 2023 Quarterly Trends Report',"Fill form of report 'Q2 2023 Quarterly Trends Report'")])


                              # ("https://skai.io/reports-and-whitepapers/get-prepped-for-prime-day-2023/", ReportsPages.fill_prime_day, Resource_download_urls.prime_day, "Prime Day 2023 Report", "Fill form of report 'Get Prepped for Prime Day 2023'"),
                              # ("https://skai.io/reports-and-whitepapers/amazon-marketing-cloud-playbook/", ReportsPages.fill_amazon_playbook, Resource_download_urls.amazon_playbook, "Amazon Marketing Cloud Playbook Report", "Fill form of report 'Amazon Marketing Cloud Playbook'"),
                              # ("https://skai.io/reports-and-whitepapers/apple-search-ads/", ReportsPages.fill_apple_ads, Resource_download_urls.apple_ads, "Apple Search Ads Report", "Fill form of report 'Mastering Apple Search Ads'")])
    def test_fill_report(self, driver, report_url, fill_method, resource_url, title, description):
        allure.dynamic.title(title)
        allure.dynamic.description(description)

        report = ReportsPages(driver, report_url)
        report.open()
        report.borlabs_banner_close()

        fill_method(report)

        report.submit_form(Button.button_contact_us)
        #
        # window_handles = driver.window_handles
        # driver.switch_to.window(window_handles[-1])
        # assert driver.current_url == resource_url
