import logging as logger
from time import sleep


class AccInfo:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.xpath_title = "//b[normalize-space()='Enter Account Information']"
        self.xpath_gender = "//input[@id='id_gender1']"
        self.xpath_password = "//input[@id='password']"
        self.xpath_day = "//div[@class='selector']/select[@id='days']/option[5]"
        self.xpath_month = "//div[@class='selector']/select[@id='months']/option[2]"
        self.xpath_years = "//div[@class='selector']/select[@id='years']/option[26]"

    def check_title(self):
        return self.driver.find_element("xpath", self.xpath_title).text

    def select_gender(self):
        self.driver.find_element("xpath", self.xpath_gender).click()

    def input_password(self, password):
        self.driver.find_element("xpath", self.xpath_password).send_keys(password)
        logger.info("Password is set")

    def date_of_birth(self):
        self.driver.find_element("xpath", self.xpath_day).click()
        logger.info("Date is selected")
        sleep(1)
        self.driver.find_element("xpath", self.xpath_month).click()
        logger.info("Month is selected")
        sleep(1)
        self.driver.find_element("xpath", self.xpath_years).click()
        logger.info("Year is selected")
