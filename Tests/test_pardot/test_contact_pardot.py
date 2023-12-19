from Pages.Pardot.pardot_contact import Pardot
from Tests.test_pardot.conftest import get_pardot, driver
from Tests.locators.pardot_locators import Contact_pardot


def test_contact_page(get_pardot):
    driver = get_pardot
    pardot = Pardot(driver, Contact_pardot.url_contact)
    pardot.contact_page()
