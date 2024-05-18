from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging as logger


class LogIn_or_SignUp:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.xpath_signInlogIn = "//a[normalize-space()='Signup / Login']"
        self.xpath_name = "//input[@placeholder='Name']"
        self.xpath_emailId = "//input[@data-qa='signup-email']"
        self.xpath_logIn_emailId = "//input[@data-qa='login-email']"
        self.xpath_logIn_password = "//input[@placeholder='Password']"
        self.xpath_sign_btn = "//div[@class='signup-form']/form/button[@class='btn btn-default']"
        self.xpath_logIn_btn = "//button[normalize-space()='Login']"
        self.xpath_exist_account = "//p[normalize-space()='Email Address already exist!']"

    def signIn_logIn(self):
        self.driver.find_element("xpath", self.xpath_signInlogIn).click()

    def logIn_mailI_and_password(self, logIn_mailId, logIn_password):
        self.driver.find_element("xpath", self.xpath_logIn_emailId).send_keys(logIn_mailId)
        sleep(2)
        self.driver.find_element("xpath", self.xpath_logIn_password).send_keys(logIn_password)

    def logIn_btn(self):
        self.driver.find_element("xpath", self.xpath_logIn_btn).click()

    def quite_logIn(self):
        self.driver.quit()

    def inputName(self, name):
        self.driver.find_element("xpath", self.xpath_name).send_keys(name)
        logger.info("Entered name is  %s", name)

    def inputEmailId(self, emaiId):
        self.driver.find_element("xpath", self.xpath_emailId).send_keys(emaiId)
        logger.info("Entered name is  %s", emaiId)

    def signIn_btn(self):
        try:
            sign_in_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_sign_btn))
            )
            sign_in_button.click()
            logger.info("Sign-in button clicked")
        except TimeoutException:
            logger.error("Timeout: Sign-in button is not clickable")

    def exist_account(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(("xpath", self.xpath_exist_account))
            )
            return self.driver.find_element("xpath", self.xpath_exist_account).text
        except TimeoutException:
            return None

