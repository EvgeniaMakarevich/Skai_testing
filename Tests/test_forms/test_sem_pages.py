from Pages.Forms.sem_pages import SemPages
from Tests.data.sem_pages_data import Urls
from conftest import driver, options
from Tests.locators.contact_page_locators import Button
from Tests.data.contact_page_data import Url
import allure
import pytest

class TestFillSemPages:
    @allure.tag("SEM Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("url, fill_method, title, description",
                             [
                                 (Urls.paid_social, SemPages.fill_sem_page_paid_social, "Paid Social SEM Page",
                                  "Fill form of SEM page 'Paid Social'"),

                                 (Urls.paid_search, SemPages.fill_sem_page_paid_search, "Paid Search SEM Page",
                                  "Fill form of SEM page 'Paid Search'"),

                                 (Urls.retail_solution, SemPages.fill_sem_page_retail_solution,
                                  "Retail Solution SEM Page", "Fill form of SEM page 'Retail Solution'"),

                                 (Urls.amazon_ads, SemPages.fill_sem_page_amazon_ads, "Amazon Ads SEM Page",
                                  "Fill form of SEM page 'Amazon Ads'")
                             ])
    def test_fill_sem_pages(self, driver, url, fill_method, title, description):
        sem_page = SemPages(driver, url)
        sem_page.open()
        driver.set_window_size(1920, 1080)
        sem_page.borlabs_banner_close()
        fill_method(sem_page)
        # sem_page.submit_form(Button.button_contact_us)
        # assert driver.current_url.startswith(Urls.thankyou_page), 'Incorrect URL'
        allure.dynamic.title(title)
        allure.dynamic.description(description)
