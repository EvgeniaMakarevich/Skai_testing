from Pages.Forms.contact_page import ContactPage
from Tests.data.Contact_page_data import Url
from Tests.locators.contact_page_locators import Fields_locators
from conftest import driver
import json

def test_submit_contact_form(driver):
    contact_page = ContactPage(driver,Fields_locators.url)
    contact_page.open()
    contact_page.borlabs_banner_close()
    contact_page.fill_contact_form()

    entered_data = contact_page.get_entered_data()
    # Открытие файла для записи
    with open('/Pages/Pardot/json_data/entered_data_contact.json', 'w') as file:
        # Запись данных в файл в формате JSON
        json.dump(entered_data, file)

    contact_page.submit_contact_form()
    assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'
    return contact_page.get_entered_data()




