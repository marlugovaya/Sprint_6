import allure

from test_page_object.locators.header_page_locators import HeaderPageLocators
from test_page_object.pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Кликаем на логотип Самоката')
    def click_scooter(self):
        self.click_on_element(HeaderPageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем на логотип Яндекса')
    def click_yandex(self):
        self.click_on_element(HeaderPageLocators.YANDEX_LOGO)