from Pages.Forms.sem_pages import SemPages
from Tests.data.sem_pages_data import Urls
from conftest import driver, options
from Tests.locators.contact_page_locators import Button


class TestFillSemPages():
    def test_paid_social(self, driver):
        paid_social = SemPages(driver, Urls.paid_social)
        paid_social.open()
        paid_social.borlabs_banner_close()
        paid_social.fill_sem_page_paid_social(driver)
        # paid_social.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'


    def test_paid_search(self, driver):
        paid_search = SemPages(driver, Urls.paid_search)
        paid_search.open()
        paid_search.borlabs_banner_close()
        paid_search.fill_sem_page_paid_search(driver)
        # paid_search.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'


    def test_retail_solution(self, driver):
        retail_solution = SemPages(driver, Urls.retail_solution)
        retail_solution.open()
        retail_solution.borlabs_banner_close()
        retail_solution.fill_sem_page_retail_solution(driver)
        # paid_search.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'


    def test_amazon_ads(self, driver):
        amazon_ads = SemPages(driver, Urls.amazon_ads)
        amazon_ads.open()
        amazon_ads.borlabs_banner_close()
        amazon_ads.fill_sem_page_amazon_ads(driver)
        # paid_search.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'

