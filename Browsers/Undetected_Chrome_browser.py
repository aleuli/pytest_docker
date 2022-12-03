import undetected_chromedriver as uc

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--incognito")
driver = uc.Chrome(executable_path='C:\\Users\\satanavsarae\\PycharmProjects\\resource\\chromedriver.exe',
                   chrome_options=options)
