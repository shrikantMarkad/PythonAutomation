import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    pass

    def orange_login(self):
        wait = WebDriverWait(self.driver, 20)
        with allure.step("Testcase executed and passed with all steps"):
            wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
            wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

