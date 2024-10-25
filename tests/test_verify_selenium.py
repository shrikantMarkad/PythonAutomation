from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

driver = None


@pytest.fixture(autouse=True)
def setup():
    print("in setup")
    option = Options()
    option.add_argument("--headless")
    global driver
    driver = webdriver.Chrome()
    yield
    driver.quit()


@pytest.mark.smoke
def test_google():
    driver.get("https://www.google.com")


@pytest.mark.smoke
def test_facebook():
    driver.get("https://www.facebook.com")


@pytest.mark.regression
def test_gmail():
    driver.get("https://www.gmail.com")
