from Pages.Forms.reports_pages import ReportsPages
from Tests.data.reports_pages_data import Urls, Resource_download_urls
from conftest import driver, options
from Tests.locators.contact_page_locators import Button
from Tests.data.contact_page_data import Url


class TestFillReportPages():
    def test_hidden_cost(self, driver):
        hidden_cost = ReportsPages(driver, Urls.hidden_cost_report)
        hidden_cost.open()
        hidden_cost.borlabs_banner_close()
        hidden_cost.fill_hidden_cost(driver)
        # hidden_cost.submit_form(Button.button_contact_us)
        # assert driver.current_url == Resource_download_urls.hidden_cost

    def test_ai(self, driver):
        ai_report = ReportsPages(driver, Urls.ai_report)
        ai_report.open()
        ai_report.borlabs_banner_close()
        ai_report.fill_ai(driver)
        # ai_report.submit_form(Button.button_contact_us)
        # assert driver.current_url == Resource_download_urls.ai

    def test_prime_day(self, driver):
        prime_day = ReportsPages(driver, Urls.prime_day)
        prime_day.open()
        prime_day.borlabs_banner_close()
        prime_day.fill_prime_day(driver)
        # prime_day.submit_form(Button.button_contact_us)
        # assert driver.current_url == Resource_download_urls.prime_day

    def test_amazon_playbook(self, driver):
        amazon_playbook = ReportsPages(driver, Urls.amazon_playbook)
        amazon_playbook.open()
        amazon_playbook.borlabs_banner_close()
        amazon_playbook.fill_amazon_playbook(driver)
        # amazon_playbook.submit_form(Button.button_contact_us)
        # assert driver.current_url == Resource_download_urls.amazon_playbook

    def test_apple_ads(self, driver):
        apple_ads = ReportsPages(driver, Urls.apple_ads)
        apple_ads.open()
        apple_ads.borlabs_banner_close()
        apple_ads.fill_apple_ads(driver)
        # apple_ads.submit_form(Button.button_contact_us)
        # assert driver.current_url == Resource_download_urls.apple_ads
