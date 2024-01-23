from Pages.Pardot.reports_pages.pardot_ai_report import PardotAi
from Pages.Pardot.reports_pages.pardot_amazon_playbook_report import PardotAmazon
from Pages.Pardot.reports_pages.pardot_apple_ads_report import PardotAppleAds
from Pages.Pardot.reports_pages.pardot_hidden_cost_report import PardotHiddenCost
from Pages.Pardot.reports_pages.pardot_prime_day_report import PardotPrimeDay
from Tests.data.reports_pages_data import Urls


class TestReportsPages():
    def test_ai_report(self, get_pardot):
        driver = get_pardot
        ai_report = PardotAi(driver, Urls.pardot_ai_form_handler)
        driver.set_window_size(1920, 1080)
        ai_report.compare_data_ai(driver)

    def test_amazon_report(self, get_pardot):
        driver = get_pardot
        amazon_report = PardotAmazon(driver, Urls.pardot_amazon_form_handler)
        driver.set_window_size(1920, 1080)
        amazon_report.compare_data_amazon_playbook(driver)

    def test_apple_ads_report(self, get_pardot):
        driver = get_pardot
        apple_ads_report = PardotAppleAds(driver, Urls.pardot_apple_ads_form_handler)
        driver.set_window_size(1920, 1080)
        apple_ads_report.compare_data_apple_ads(driver)

    def test_hidden_cost_report(self, get_pardot):
        driver = get_pardot
        hidden_cost_report = PardotHiddenCost(driver, Urls.pardot_hidden_cost_handler)
        driver.set_window_size(1920, 1080)
        hidden_cost_report.compare_data_hidden_cost(driver)

    # def test_prime_day_report(self, get_pardot):
    #     driver = get_pardot
    #     prime_day_report = PardotPrimeDay(driver, Urls.pardot_prime_day_form_handler)
    #     driver.set_window_size(1920, 1080)
    #     prime_day_report.compare_data_prime_day(driver)
