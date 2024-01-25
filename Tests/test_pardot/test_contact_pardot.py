from Pages.Pardot.pardot_contact_page import PardotContactPage
from Tests.test_pardot.conftest import get_pardot, browser
from Tests.locators.pardot_locators import Contact_pardot
import allure

@allure.tag("Contact form")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Contact form')
@allure.description('Compare pardot data with entered contact form data')
def test_contact_page(get_pardot):
    driver = get_pardot
    pardot = PardotContactPage(driver, Contact_pardot.url_contact)
    driver.set_window_size(1920, 1080)
    pardot.compare_data_contact_page(driver)
