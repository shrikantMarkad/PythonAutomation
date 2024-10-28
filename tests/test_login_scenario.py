import logging
import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from tests.basetest import BaseTest

LOGGER = logging.getLogger(__name__)


@pytest.mark.usefixtures("log_on_failure")
class TestSelenium(BaseTest):

    @pytest.mark.parametrize("ss", ["e", "h"])
    def test_login_00(self, ss):
        wait = WebDriverWait(self.driver, 20)
        with allure.step("Testcase executed and passed with all steps"):
            self.orange_login()
            assert self.driver.title == "OrangeHRM", "Home page title does not matched"

        #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[placeholder = 'Search']"))).send_keys(
        #         "Time")
        # with allure.step("Search with time parameter"):
        #     self.driver.find_element(By.XPATH, "//span[text()='Time']").click()
        #
        #     actions = ActionChains(self.driver)
        #
        #     wait.until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, "[placeholder = 'Type for hints...']"))).send_keys(
        #         "Shrikant")
        # with allure.step("Submit the result"):
        #     element = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")
        #
        #     actions.click(element)

    @pytest.mark.parametrize("ss", ["e", "h"])
    def test_login_1(self, ss):
        with allure.step("Testcase executed and passed with all steps"):
            self.orange_login()
            assert self.driver.title == "OrangeHRM", "Home page title does not matched"

    @pytest.mark.parametrize("ss", ["e", "h"])
    def test_login_2(self, ss):
        with allure.step("Testcase executed and passed with all steps"):
            self.orange_login()
            assert self.driver.title == "OrangeHRM1", "Home page title does not matched"

    @pytest.mark.parametrize("ss", ["e", "h"])
    def test_login_3(self, ss):
        with allure.step("Testcase executed and passed with all steps"):
            self.orange_login()
            assert self.driver.title == "OrangeHRM", "Home page title does not matched"

