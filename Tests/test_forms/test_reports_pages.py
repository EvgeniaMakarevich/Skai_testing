from Pages.Forms.reports_pages import ReportsPages
from Tests.data.reports_pages_data import Urls, Resource_download_urls
from conftest import driver, options
from Tests.locators.contact_page_locators import Button
import allure
import pytest



class TestFillReportPages():
    @allure.tag("Report form")
    @allure.severity(allure.severity_level.CRITICAL)

    @pytest.mark.parametrize("report_url, fill_method, resource_url, title, description",
                             [("https://skai.io/reports-and-whitepapers/the-hidden-cost-of-advertising-point-solutions/", ReportsPages.fill_hidden_cost, Resource_download_urls.hidden_cost, "Hidden Cost Report", "Fill form of report 'The Hidden Cost of Advertising Point Solutions'"),
                              ("https://skai.io/reports-and-whitepapers/embracing-generative-ai/", ReportsPages.fill_ai, Resource_download_urls.ai, "Generative AI Report", "Fill form of report 'The Next Big Thing: Where Generative AI’s..'"),
                              ("https://skai.io/reports-and-whitepapers/get-prepped-for-prime-day-2023/", ReportsPages.fill_prime_day, Resource_download_urls.prime_day, "Prime Day 2023 Report", "Fill form of report 'Get Prepped for Prime Day 2023'"),
                              ("https://skai.io/reports-and-whitepapers/amazon-marketing-cloud-playbook/", ReportsPages.fill_amazon_playbook, Resource_download_urls.amazon_playbook, "Amazon Marketing Cloud Playbook Report", "Fill form of report 'Amazon Marketing Cloud Playbook'"),
                              ("https://skai.io/reports-and-whitepapers/apple-search-ads/", ReportsPages.fill_apple_ads, Resource_download_urls.apple_ads, "Apple Search Ads Report", "Fill form of report 'Mastering Apple Search Ads'")])
    def test_fill_report(self, driver, report_url, fill_method, resource_url, title, description):
        report = ReportsPages(driver, report_url)
        report.open()
        report.borlabs_banner_close()

        allure.dynamic.title(title)
        allure.dynamic.description(description)

        fill_method(report)

        # report.submit_form(Button.button_contact_us)
        #
        # window_handles = driver.window_handles
        # driver.switch_to.window(window_handles[-1])
        # assert driver.current_url == resource_url
















# class TestFillReportPages():
    # @allure.title('The Hidden Cost of Advertising Point Solutions')
    # @allure.description("Fill form of report 'The Hidden Cost of Advertising Point Solutions'")
    # @allure.tag("Report form")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.link("https://skai.io/reports-and-whitepapers/the-hidden-cost-of-advertising-point-solutions/", name="Report page")
    # def test_hidden_cost(self, driver):
    #     hidden_cost = ReportsPages(driver, Urls.hidden_cost_report)
    #     hidden_cost.open()
    #     hidden_cost.borlabs_banner_close()
    #     hidden_cost.fill_hidden_cost(driver)
    #     # hidden_cost.submit_form(Button.button_contact_us)
    #     #
    #     # window_handles = driver.window_handles
    #     # driver.switch_to.window(window_handles[-1])
    #     # assert driver.current_url == Resource_download_urls.hidden_cost
    #
    # @allure.title('The Next Big Thing: Where Generative AI’s..')
    # @allure.description("Fill form of report 'The Next Big Thing: Where Generative AI’s..'")
    # @allure.tag("Report form")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.link("https://skai.io/reports-and-whitepapers/embracing-generative-ai/", name="Report page")
    # def test_ai(self, driver):
    #     ai_report = ReportsPages(driver, Urls.ai_report)
    #     ai_report.open()
    #     ai_report.borlabs_banner_close()
    #     ai_report.fill_ai(driver)
    #     # ai_report.submit_form(Button.button_contact_us)
    #     #
    #     # window_handles = driver.window_handles
    #     # driver.switch_to.window(window_handles[-1])
    #     # assert driver.current_url == Resource_download_urls.ai
    #
    # @allure.title('Get Prepped for Prime Day 2023')
    # @allure.description("Fill form of report 'Get Prepped for Prime Day 2023'")
    # @allure.tag("Report form")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.link("https://skai.io/reports-and-whitepapers/get-prepped-for-prime-day-2023/", name="Report page")
    # def test_prime_day(self, driver):
    #     prime_day = ReportsPages(driver, Urls.prime_day)
    #     prime_day.open()
    #     prime_day.borlabs_banner_close()
    #     prime_day.fill_prime_day(driver)
    #     # prime_day.submit_form(Button.button_contact_us)
    #     #
    #     # window_handles = driver.window_handles
    #     # driver.switch_to.window(window_handles[-1])
    #     # assert driver.current_url == Resource_download_urls.prime_day
    #
    #
    # @allure.title('Amazon Marketing Cloud Playbook')
    # @allure.description("Fill form of report 'Amazon Marketing Cloud Playbook'")
    # @allure.tag("Report form")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.link("https://skai.io/reports-and-whitepapers/amazon-marketing-cloud-playbook/", name="Report page")
    # def test_amazon_playbook(self, driver):
    #     amazon_playbook = ReportsPages(driver, Urls.amazon_playbook)
    #     amazon_playbook.open()
    #     amazon_playbook.borlabs_banner_close()
    #     amazon_playbook.fill_amazon_playbook(driver)
    #     # amazon_playbook.submit_form(Button.button_contact_us)
    #     #
    #     # window_handles = driver.window_handles
    #     # driver.switch_to.window(window_handles[-1])
    #     # assert driver.current_url == Resource_download_urls.amazon_playbook
    #
    # @allure.title('Mastering Apple Search Ads')
    # @allure.description("Fill form of report 'Mastering Apple Search Ads'")
    # @allure.tag("Report form")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.link("https://skai.io/reports-and-whitepapers/apple-search-ads/", name="Report page")
    # def test_apple_ads(self, driver):
    #     apple_ads = ReportsPages(driver, Urls.apple_ads)
    #     apple_ads.open()
    #     apple_ads.borlabs_banner_close()
    #     apple_ads.fill_apple_ads(driver)
    #     # apple_ads.submit_form(Button.button_contact_us)
    #     #
    #     # window_handles = driver.window_handles
    #     # driver.switch_to.window(window_handles[-1])
    #     # assert driver.current_url == Resource_download_urls.apple_ads
