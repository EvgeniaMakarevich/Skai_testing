from Pages.Forms.contact_page import ContactPageMain
from Tests.data.contact_page_data import Url
from Tests.locators.contact_page_locators import Button
from conftest import driver, options
import allure

@allure.tag("Contact form")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Contact form')
@allure.description('Fill contact form')
def test_submit_contact_main(driver):
    contact_page = ContactPageMain(driver, Url.url_contact_main)
    contact_page.open()
    driver.set_window_size(1920, 1080)
    contact_page.borlabs_banner_close()
    # contact_page.fill_contact_main(driver)
    #
    # contact_page.submit_form(Button.button_contact_us)
    # assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'
