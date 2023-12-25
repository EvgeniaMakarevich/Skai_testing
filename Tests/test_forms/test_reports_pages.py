from Pages.Forms.reports_pages import ReportsPages
from Tests.data.reports_pages_data import Urls
from conftest import driver, options
from Tests.locators.contact_page_locators import Button


class TestFillReportPages():
    def test_hidden_cost(self, driver):
        hidden_cost = ReportsPages(driver, Urls.hidden_cost_report)
        hidden_cost.open()
        hidden_cost.borlabs_banner_close()
        hidden_cost.fill_hidden_cost(driver)
        # hidden_cos.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'

    def test_ai(self, driver):
        ai_report = ReportsPages(driver, Urls.ai_report)
        ai_report.open()
        ai_report.borlabs_banner_close()
        ai_report.fill_ai(driver)
        # hidden_cos.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'


    def test_prime_day(self, driver):
        prime_day = ReportsPages(driver, Urls.prime_day)
        prime_day.open()
        prime_day.borlabs_banner_close()
        prime_day.fill_prime_day(driver)
        # hidden_cos.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'


    def test_amazon_playbook(self, driver):
        amazon_playbook = ReportsPages(driver, Urls.amazon_playbook)
        amazon_playbook.open()
        amazon_playbook.borlabs_banner_close()
        amazon_playbook.fill_amazon_playbook(driver)
        # hidden_cos.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'


    def test_apple_ads(self, driver):
        apple_ads = ReportsPages(driver, Urls.apple_ads)
        apple_ads.open()
        apple_ads.borlabs_banner_close()
        apple_ads.fill_apple_ads(driver)
        # hidden_cos.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'