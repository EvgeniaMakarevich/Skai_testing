from Tests.data.events_pages_data import Pardot
from Tests.data.events_pages_data import Json_path
from Pages.Pardot.Base_events_page import PardotBaseEvent
import allure


class EventPagesPardot(PardotBaseEvent):
    @allure.step("Compare data 'Media Leaders Roundtable' event")
    def compare_data_media_roundtable(self, driver):
        media_roundtable = PardotBaseEvent(driver, Pardot.media_roundtable_form_handler)
        contact_data_media_roundtable = self.load_json_data_events(Json_path.media_roundtable_event_pardot)
        media_roundtable.compare_data_1(contact_data_media_roundtable)

    @allure.step("Compare data 'Iderive' event")
    def compare_data_iderive(self, driver):
        idervie = PardotBaseEvent(driver, Pardot.iderive_form_handler)
        contact_data_idervie = self.load_json_data_events(Json_path.iderive_event)
        idervie.compare_data_1(contact_data_idervie)

    @allure.step("Compare data 'Meet Skai at Shoptalk US' event")
    def compare_data_shoptalk(self, driver):
        shoptalk = PardotBaseEvent(driver, Pardot.shoptalk_form_handler)
        contact_data_shoptalk = self.load_json_data_events(Json_path.shoptalk_event)
        shoptalk.compare_data_2(contact_data_shoptalk)
