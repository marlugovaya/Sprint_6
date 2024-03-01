
from test_page_object.locators.dzen_page_locators import DzenPageLocators
from test_page_object.pages.base_page import BasePage


class DzenPage(BasePage):
    def dzen_page_opened(self):
        self.move_to_next_tab()
        return self.get_text_from_element(DzenPageLocators.DZEN_NEWS_BUTTON)
