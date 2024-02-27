from Tests.data.events_pages_data import Pardot
from Pages.Pardot.events_pages import EventPagesPardot
import allure
import pytest


class TestEventsPages:
    @allure.tag("Compare Pardot data with entered Events data")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('Form_handler_url,fill_method, title, description', [
        (Pardot.media_roundtable_form_handler, EventPagesPardot.compare_data_media_roundtable, "Media Leaders Roundtable Event",
         "Compare Pardot data with entered 'Media Leaders Roundtable Event' data"),
        (Pardot.iderive_form_handler, EventPagesPardot.compare_data_iderive,
         "iDerive Event",
         "Compare Pardot data with entered 'iDerive' data")
    ])
    def test_compare_event_data(self, get_pardot, Form_handler_url, fill_method, title, description):
        allure.dynamic.title(title)
        allure.dynamic.description(description)
        driver = get_pardot
        event = EventPagesPardot(driver, Form_handler_url)
        driver.set_window_size(1920, 1080)
        fill_method(event, driver)
