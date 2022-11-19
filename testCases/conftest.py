# This file contains fixtures which are common for all the test cases
# These steps are common in every test case

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup(browser): # This function allow user to select respective browsers
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        print("Launching Chrome Browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        driver.maximize_window()
        print("Launching Edge Browser")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):    # This will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):   # This will return the browser value to setup method
    return request.config.getoption("--browser")

########## pyTest HTML Report ##########


# It is a hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'eCommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ammar'


# It is a hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
