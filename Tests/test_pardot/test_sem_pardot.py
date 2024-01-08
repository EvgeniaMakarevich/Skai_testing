from Pages.Pardot.sem_pages.pardot_paid_social import PardotPaidSocial
from Pages.Pardot.sem_pages.pardot_paid_search import PardotPaidSearch
from Pages.Pardot.sem_pages.pardot_retail_solution import PardotRetailSolution
from Pages.Pardot.sem_pages.pardot_amazon_ads import PardotAmazonAds
from Tests.locators.pardot_locators import Contact_pardot


class TestSemPages():
    def test_paid_social(self, get_pardot):
        driver = get_pardot
        paid_social = PardotPaidSocial(driver, Contact_pardot.url_contact)
        driver.set_window_size(1920, 1080)
        paid_social.compare_data_paid_social(driver)

    def test_paid_search(self, get_pardot):
        driver = get_pardot
        paid_social = PardotPaidSearch(driver, Contact_pardot.url_contact)
        driver.set_window_size(1920, 1080)
        paid_social.compare_data_paid_search(driver)


    def test_retail_solution(self, get_pardot):
        driver = get_pardot
        retail_solution = PardotRetailSolution(driver, Contact_pardot.url_contact)
        driver.set_window_size(1920, 1080)
        retail_solution.compare_data_retail_solution(driver)


    def test_amazon_ads(self, get_pardot):
        driver = get_pardot
        amazon_ads = PardotAmazonAds(driver, Contact_pardot.url_contact)
        driver.set_window_size(1920, 1080)
        amazon_ads.compare_data_amazon_ads(driver)

