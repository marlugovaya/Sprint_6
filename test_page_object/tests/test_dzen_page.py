import allure

from test_page_object.pages.dzen_page import DzenPage

class TestDzenPage:
    @allure.title('Проверка нажатия на логотип Яндекса.')
    def test_click_yandex_logo(self, header_page, main_page, dzen_page):
        header_page.click_yandex()
        assert dzen_page.dzen_page_opened() == 'Новости'

