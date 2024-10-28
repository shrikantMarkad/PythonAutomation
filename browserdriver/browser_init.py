
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserInit:
    _driver = None
    option = Options()

    @staticmethod
    def create_driver_instance():
        BrowserInit.option.add_argument("--headless")
        BrowserInit._driver = webdriver.Chrome()
        BrowserInit._driver.get("https://opensource-demo.orangehrmlive.com/")
        return BrowserInit._driver

    @staticmethod
    def get_driver():
        return BrowserInit.driver



