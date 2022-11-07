# This file contains fixtures which are common for all the test cases
# These steps are common in every test case

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup(browser):
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

# It is a hook for adding enviroment info to HTML report
