import time

from selenium.webdriver import ActionChains, Keys


class Base:

    def __init__(self, driver):
        self.driver = driver

    # Method get_current_url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    # Method assert word
    @staticmethod
    def assert_word(word, result):
        value_word = word.text
        assert value_word == result
        print("Value word: OK")

    # Method assert_current_url
    def assert_current_url(self, url):
        time.sleep(3)
        assert self.driver.current_url == url
        print(f"{url} assert")

    # Method action return
    def action_return(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.RETURN).perform()
        print(f"Action return: OK")

    # Method move to element
    def action_move_to_element(self, elem):
        action = ActionChains(self.driver)
        action.move_to_element(elem).perform()
        print(f" Move to elem: OK")
