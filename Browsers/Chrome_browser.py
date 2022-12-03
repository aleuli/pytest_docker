from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path='C:\\Users\\satanavsarae\\PycharmProjects\\resource\\chromedriver.exe',
                          chrome_options=options)
