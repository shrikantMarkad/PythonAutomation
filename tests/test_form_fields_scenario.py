import logging
import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from urllib3.util import request

from browserdriver.browser_init import BrowserInit
from tests.basetest import BaseTest

LOGGER = logging.getLogger(__name__)


@pytest.mark.usefixtures("log_on_failure")
class TestOrange(BaseTest):

    @pytest.mark.parametrize("ss", ["e", "h"])
    def test_orange_login_00(self, ss):
        with allure.step("Testcase executed and passed with all steps"):
            self.orange_login()
            assert self.driver.title == "OrangeHRM", "Home page title does not matched"

