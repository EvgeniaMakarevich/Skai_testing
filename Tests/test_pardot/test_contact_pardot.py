from Pages.Pardot.pardot_contact_page import PardotContactPage
from Tests.test_pardot.conftest import get_pardot, browser
from Tests.locators.pardot_locators import Contact_pardot


def test_contact_page(get_pardot):
    driver = get_pardot
    pardot = PardotContactPage(driver, Contact_pardot.url_contact)
    pardot.compare_data_contact_page(driver)
