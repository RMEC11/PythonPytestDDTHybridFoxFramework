import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ReadConfiguration
import allure

driver = None

@pytest.fixture()
def log_on_failure(request):
    yield
    item=request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Failed Scenario", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    outcome =yield
    rep=outcome.get_result()
    setattr(item,"rep_"+rep.when,rep)
    return rep


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser_name = ReadConfiguration.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("Browser Name not found in Basic Info list")

    driver.maximize_window()
    base_url = ReadConfiguration.read_configuration("basic info", "url")
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()
