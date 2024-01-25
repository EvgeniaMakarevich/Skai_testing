from Tests.locators.pardot_locators import Contact_pardot
from Tests.data.sem_pages_data import Urls
from Pages.Pardot.Base_pardot_contact import PardotBaseContact
from Tests.data.sem_pages_data import Json_path
import allure

class SemPagesPardot(PardotBaseContact):
    @allure.step("Comparing Amazon Ads data")
    def compare_data_amazon_ads(self, driver):
        amazon_ads = PardotBaseContact(driver, Contact_pardot.url_contact)
        contact_data_amazon_ads = self.load_json_data(Json_path.amazon_ads_pardot)
        amazon_ads.compare_data(contact_data_amazon_ads)
        amazon_ads.compare_page_url(Contact_pardot.page_url, Urls.amazon_ads_url)

    @allure.step("Comparing Paid Search data")
    def compare_data_paid_search(self, driver):
        paid_search = PardotBaseContact(driver, Contact_pardot.url_contact)
        contact_data_paid_search = self.load_json_data(Json_path.paid_search_pardot)
        paid_search.compare_data(contact_data_paid_search)
        paid_search.compare_page_url(Contact_pardot.page_url, Urls.paid_search_url)

    @allure.step("Comparing Paid Social data")
    def compare_data_paid_social(self, driver):
        paid_social = PardotBaseContact(driver, Contact_pardot.url_contact)
        contact_data_paid_social = self.load_json_data(Json_path.paid_social_pardot)
        paid_social.compare_data(contact_data_paid_social)
        paid_social.compare_page_url(Contact_pardot.page_url, Urls.paid_social_url)

    @allure.step("Comparing Retail Solution data")
    def compare_data_retail_solution(self, driver):
        retail_solution = PardotBaseContact(driver, Contact_pardot.url_contact)
        contact_data_retail_solution = self.load_json_data(Json_path.retail_solution_pardot)
        retail_solution.compare_data(contact_data_retail_solution)
        retail_solution.compare_page_url(Contact_pardot.page_url, Urls.retail_solution_url)
