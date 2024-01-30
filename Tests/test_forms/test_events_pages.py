from Pages.Forms.events_pages import EventsPages
from Tests.data.events_pages_data import Urls
from conftest import driver, options
from Tests.locators.events_locators import EventFormLocators
import allure
import pytest

locators = EventFormLocators()


class TestFillEventPages:
    @allure.tag("Event Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("url, fill_method, title, description",
                             [
                                 (Urls.media_roundtable_url, EventsPages.fill_media_roundtable, "Media Leaders Roundtable Event Page",
                                  "Fill form of Event page 'Media Leaders Roundtable'"),
                             ])
    def test_fill_event_pages(self, driver, url, fill_method, title, description):
        allure.dynamic.title(title)
        allure.dynamic.description(description)
        event = EventsPages(driver, url)
        driver.set_window_size(1920, 1080)
        event.open()
        event.borlabs_banner_close()
        fill_method(event)

        event.submit_form(locators.submit_button)
        assert driver.current_url.startswith(Urls.thankyou), 'Incorrect URL'