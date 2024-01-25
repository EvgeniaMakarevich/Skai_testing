from Pages.Pardot.sem_pages import SemPagesPardot
from Tests.locators.pardot_locators import Contact_pardot
import allure
import pytest


class TestSemPages:
    @allure.tag("Compare Pardot data with entered Sem Pages data")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('Form_handler_url,fill_method, title, description', [

        (Contact_pardot.url_contact, SemPagesPardot.compare_data_paid_social, "Paid Social SEM Page",
         "Compare Pardot data with entered 'Paid Social SEM Page' data"),

        (Contact_pardot.url_contact, SemPagesPardot.compare_data_paid_search,
         "Paid Search SEM Page",
         "Compare Pardot data with entered 'Paid Search SEM Page' data"),

        (Contact_pardot.url_contact, SemPagesPardot.compare_data_retail_solution, "Retail Solution SEM Page",
         "Compare Pardot data with entered 'Retail Solution SEM Page' data"),

        (Contact_pardot.url_contact, SemPagesPardot.compare_data_amazon_ads, "Amazon Ads SEM Page",
         "Amazon Ads SEM Page' data")
         ])
    def test_compare_sem_data(self, get_pardot, Form_handler_url, fill_method, title, description):
        allure.dynamic.title(title)
        allure.dynamic.description(description)
        driver = get_pardot
        sem = SemPagesPardot(driver, Form_handler_url)
        driver.set_window_size(1920, 1080)
        fill_method(sem, driver)