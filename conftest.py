import pytest
from selenium import webdriver

from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.dzen_page import DzenPage
from test_page_object.pages.header_page import HeaderPage
from test_page_object.pages.main_page import MainPage
from test_page_object.pages.order_page import OrderPage


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope='function')
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture(scope='function')
def header_page(driver):
    return HeaderPage(driver)

@pytest.fixture(scope='function')
def dzen_page(driver):
    return DzenPage(driver)