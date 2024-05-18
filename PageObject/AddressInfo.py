import logging as logger
from time import sleep


class AddInfo:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.xpath_title = "//b[normalize-space()='Address Information']"
        self.xpath_firstName = "//input[@id='first_name']"
        self.xpath_lastName = "//input[@id='last_name']"
        self.xpath_compony = "//input[@id='company']"
        self.xpath_address = "//input[@id='address1']"
        self.xpath_country = "//select[@id='country']/option[1]"
        self.xpath_state = "//input[@id='state']"
        self.xpath_city = "//input[@id='city']"
        self.xpath_zipCode = "//input[@id='zipcode']"
        self.xpath_mobileNo = "//input[@id='mobile_number']"
        self.xpath_create_acc_btn = "//button[normalize-space()='Create Account']"
        self.xpath_success_msg = "//b[normalize-space()='Account Created!']"
        self.xpath_continue_btn = "//a[@data-qa='continue-button']"

    def check_title(self):
        return self.driver.find_element("xpath", self.xpath_title).text

    def fullName(self, firstName, lastName):
        self.driver.find_element("xpath", self.xpath_firstName).send_keys(firstName)
        logger.info("Entered first name is %s", firstName)
        sleep(1)
        self.driver.find_element("xpath", self.xpath_lastName).send_keys(lastName)
        logger.info("Entered last name is %s", lastName)

    def companyName_with_address(self, companyName, address):
        self.driver.find_element("xpath", self.xpath_compony).send_keys(companyName)
        logger.info("Entered company name is %s", companyName)
        sleep(1)
        self.driver.find_element("xpath", self.xpath_address).send_keys(address)
        logger.info("Entered company name is %s", address)

    def select_country(self):
        self.driver.find_element("xpath", self.xpath_country).click()

    def state_and_city_name(self, stateName, cityName):
        self.driver.find_element("xpath", self.xpath_state).send_keys(stateName)
        logger.info("Entered company name is %s", stateName)
        sleep(1)
        self.driver.find_element("xpath", self.xpath_city).send_keys(cityName)
        logger.info("Entered company name is %s", cityName)

    def zipCode_and_mobileNo(self, zipCode, mobileNo):
        self.driver.find_element("xpath", self.xpath_zipCode).send_keys(zipCode)
        logger.info("Entered company name is %s", zipCode)
        sleep(1)
        self.driver.find_element("xpath", self.xpath_mobileNo).send_keys(mobileNo)
        logger.info("Entered company name is %s", mobileNo)

    def createAcc_btn(self):
        self.driver.find_element("xpath", self.xpath_create_acc_btn).click()
        logger.info("Your account get create successfully")

    def check_msg(self):
        return self.driver.find_element("xpath", self.xpath_success_msg).text

    def click_continue(self):
        self.driver.find_element("xpath", self.xpath_continue_btn).click()