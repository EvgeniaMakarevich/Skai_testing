from Pages.Forms.sem_pages import SemPages
from Tests.data.sem_pages_data import Urls
from conftest import driver, options
from Tests.locators.contact_page_locators import Button
from Tests.data.contact_page_data import Url


class TestFillSemPages():
    def test_paid_social(self, driver):
        paid_social = SemPages(driver, Urls.paid_social)
        paid_social.open()
        driver.set_window_size(1920, 1080)
        paid_social.borlabs_banner_close()
        paid_social.fill_sem_page_paid_social(driver)
        # paid_social.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'


    def test_paid_search(self, driver):
        paid_search = SemPages(driver, Urls.paid_search)
        paid_search.open()
        driver.set_window_size(1920, 1080)
        paid_search.borlabs_banner_close()
        paid_search.fill_sem_page_paid_search(driver)
        # paid_search.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'


    def test_retail_solution(self, driver):
        retail_solution = SemPages(driver, Urls.retail_solution)
        retail_solution.open()
        driver.set_window_size(1920, 1080)
        retail_solution.borlabs_banner_close()
        retail_solution.fill_sem_page_retail_solution(driver)
        # retail_solution.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'


    def test_amazon_ads(self, driver):
        amazon_ads = SemPages(driver, Urls.amazon_ads)
        amazon_ads.open()
        driver.set_window_size(1920, 1080)
        amazon_ads.borlabs_banner_close()
        amazon_ads.fill_sem_page_amazon_ads(driver)
        # amazon_ads.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'

