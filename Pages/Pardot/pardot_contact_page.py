from Tests.locators.pardot_locators import Contact_pardot
from Pages.Pardot.Base_pardot_contact import PardotBaseContact
from Tests.data.contact_page_data import Url
from Tests.data.contact_page_data import Json_path
import allure
class PardotContactPage(PardotBaseContact):
    @allure.step("Comparing contact data")
    def compare_data_contact_page(self, driver):
        contact_page = PardotBaseContact(driver, Contact_pardot.url_contact)
        contact_data_main_contact = contact_page.load_json_data(Json_path.contact_page_main)
        contact_page.compare_data(contact_data_main_contact)
        contact_page.compare_page_url(Contact_pardot.page_url, Url.page_url)




