import time
import allure

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    # Urls
    url_main_page = "https://www.dns-shop.ru/"

    # Locators
    city_menu = "//div[@class='city-select__label']/span[2]"
    district_centre = "//ul[@class='districts']/li[7]"
    region_voronesh = "//ul[@class='regions']/li[4]"
    city_Bobrov = "//ul[@class='cities']/li[4]"
    input_field = "//input[@type='search'] [@id='null']"
    input_field_2 = "//form[@class='presearch']/div/input"
    button_every_right = "//div[@class='v-confirm-city__buttons']/button[1]"
    payment = "//span[contains(text(),'Оплата')]"
    button_buy_first_product = "//*[@id='search-results']/div[2]/div/div[1]/div[1]/div[4]/button[2]"
    amount_basket = "//div[@class='buttons']/a/span[@class='cart-link__badge']"

    # Assert text
    assert_city_Bobrov = "Бобров"
    assert_amount_basket = "1"

    # Assert url
    assert_url_iphone13 = "https://www.dns-shop.ru/search/?q=Iphone+13+pro&category=17a8a01d16404e77"
    assert_payment_url = "https://www.dns-shop.ru/im_payment/"

    # Getters
    def get_city_menu(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.city_menu)))

    def get_district_centre(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.district_centre)))

    def get_region_voronesh(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.region_voronesh)))

    def get_city_bobrov(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.city_Bobrov)))

    def get_input_field(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.input_field)))

    def get_input_field_2(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.input_field_2)))

    def get_button_every_right(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_every_right)))

    def get_payment(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.payment)))

    def get_button_buy_first_product(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_buy_first_product)))

    def get_amount_basket(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.amount_basket)))

    # Actions
    def click_city_menu(self):
        self.get_city_menu().click()
        print("Menu city click: OK")

    def click_district_centre(self):
        self.get_district_centre().click()
        print("District centre click: OK")

    def click_region_voronesh(self):
        self.get_region_voronesh().click()
        print("Region Voronesh click: OK")

    def click_city_bobrov(self):
        self.get_city_bobrov().click()
        print("Bobrov city click: OK")

    def enter_input_field(self):
        self.get_input_field().send_keys("Iphone 13 pro")
        print("Enter text in input field: OK")

    def enter_input_field_2(self):
        self.get_input_field_2().send_keys("Iphone 13 pro")
        print("Enter text in input field: OK")

    def click_button_er(self):
        self.get_button_every_right().click()
        print("Button every right: OK")

    def click_button_buy_first_product(self):
        self.get_button_buy_first_product().click()
        print("Iphone add basket: OK")

    # Methods
    def open_main_page(self):
        with allure.step("open_main_page"):
            Logger.add_start_step(method="open_main_page")
            self.driver.get(self.url_main_page)
            self.driver.maximize_window()
            self.assert_current_url(url=self.url_main_page)
            Logger.add_end_step(url=self.driver.current_url, method="open_main_page")

    def select_city(self):
        with allure.step("select_city"):
            Logger.add_start_step(method="select_city")
            self.driver.get(self.url_main_page)
            self.driver.maximize_window()
            self.assert_current_url(url=self.url_main_page)
            self.click_city_menu()
            self.click_district_centre()
            self.click_region_voronesh()
            self.click_city_bobrov()
            try:
                self.assert_word(self.get_city_menu(), self.assert_city_Bobrov)
            except AttributeError:
                print("I have issue: AttributeError, this isn't Bobrov")
                Logger.add_end_step(url=self.driver.current_url, method="select_city")

    def input_text(self):
        with allure.step("input_text"):
            Logger.add_start_step(method="input_text")
            self.driver.get(self.url_main_page)
            self.driver.maximize_window()
            self.assert_current_url(url=self.url_main_page)
            try:
                self.enter_input_field()
            except TimeoutException:
                self.enter_input_field_2()
            self.action_return()
            self.assert_current_url(self.assert_url_iphone13)
            Logger.add_end_step(url=self.driver.current_url, method="input_text")

    def enter_payment(self):
        with allure.step("enter_payment"):
            Logger.add_start_step(method="enter_payment")
            self.driver.get(self.url_main_page)
            self.driver.maximize_window()
            self.assert_current_url(url=self.url_main_page)
            self.action_move_to_element(self.get_payment())
            self.get_payment().click()
            self.assert_current_url(self.assert_payment_url)
            Logger.add_end_step(url=self.driver.current_url, method="enter_payment")

    def buy_product(self):
        with allure.step("buy_product"):
            Logger.add_start_step(method="buy_product")
            self.input_text()
            self.click_button_buy_first_product()
            time.sleep(2)
            self.driver.back()
            self.assert_word(self.get_amount_basket(), self.assert_amount_basket)
            Logger.add_end_step(url=self.driver.current_url, method="buy_product")
