from test_page_object.locators.header_page_locators import HeaderPageLocators
from test_page_object.pages.base_page import BasePage


class HeaderPage(BasePage):
    def click_scooter(self):
        self.click_on_element(HeaderPageLocators.SCOOTER_LOGO)

    def click_yandex(self):
        self.click_on_element(HeaderPageLocators.YANDEX_LOGO)