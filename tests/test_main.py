from Browsers.Chrome_browser import *
from pages.main_page import MainPage


MainPage_class = MainPage(driver)


# tests
def test_open_main_page():
    MainPage_class.open_main_page()


def test_select_city():
    MainPage_class.select_city()


def test_input_field():
    MainPage_class.input_text()


def test_click_payment():
    MainPage_class.enter_payment()


def test_buy_product():
    MainPage_class.buy_product()
