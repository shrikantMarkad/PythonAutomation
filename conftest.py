import pytest
import allure
from datetime import datetime
from selenium import webdriver
from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def log_on_failure(request):
    yield
    item = request.node
    test_name = str(item.nodeid).split("::")[-1]
    print(f"test {test_name} failed and path to the test is {item.nodeid}")
    if item.rep_call.failed:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        allure.attach(request.cls.driver.get_screenshot_as_png(), name=test_name+"_"+now, attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome"])
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    request.cls.driver = driver
    yield
    driver.quit()
