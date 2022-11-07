
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:   # Test case ID is being provided
    # Calling common variable through utility file readProperties.py
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home page Title Test Is Passed **********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home Page Title Test is Failed **********")
            assert False

    def test_login(self, setup):
        self.logger.info("********** Verifying Login Details **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)   # Calling constructor from LoginPage class
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** Login Test Is Passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_homePageTitle.png")
            self.logger.error("********** Login Test Is Failed **********")
            self.driver.close()
            assert False


