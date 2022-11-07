from selenium import webdriver


class LoginPage:
    # Identify all the locators for login and logout page
    textBox_userName_id = "Email"
    textBox_password_id = "Password"
    button_login_xPath = "//button[@type='submit']"
    link_logout_linkText = "Logout"

    # Create a constructor to initialize the driver
    # Capture the driver from the test case and will pass this driver later
    # and that driver will be initiating the class variable
    def __init__(self,driver):  # => this driver will come from the actual test case
        self.driver = driver    # => This driver will initiate our local driver

    def setUserName(self, username):    # Username will come from the actual test case
        self.driver.find_element("id", self.textBox_userName_id).clear()
        self.driver.find_element("id", self.textBox_userName_id).send_keys(username)

    def setPassword(self, password):    # Password will come from the actual test case
        self.driver.find_element("id", self.textBox_password_id).clear()
        self.driver.find_element("id", self.textBox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath", self.button_login_xPath).click()

    def clickLogout(self):
        self.driver.find_element("link text", self.link_logout_linkText).click()

