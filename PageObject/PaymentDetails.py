from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentDetails:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.xpath_name_on_card = "//input[@name='name_on_card']"
        self.xpath_card_number = "//input[@name='card_number']"
        self.xpath_cvc = "//input[@placeholder='ex. 311']"
        self.xpath_month = "//input[@placeholder='MM']"
        self.xpath_year = "//input[@placeholder='YYYY']"
        self.xpath_pay_and_confirm_order = "//button[@id='submit']"
        self.xpath_orderPlaced = "//b[normalize-space()='Order Placed!']"
        self.xpath_download_invoice = "//a[normalize-space()='Download Invoice']"
        self.xpath_continue = "//a[normalize-space()='Continue']"

    def name_and_cardDetails(self, name, cardNo, cvc, month, year):
        # name on card
        nameOnCard = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_name_on_card))
            )
        nameOnCard.send_keys(name)
        sleep(1)

        # card number
        cardNumber = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_card_number))
            )
        cardNumber.send_keys(cardNo)
        sleep(1)

        # cvc
        cvcNo = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_cvc))
            )
        cvcNo.send_keys(cvc)
        sleep(1)

        # month
        expMonth = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_month))
            )
        expMonth.send_keys(month)
        sleep(1)

        # year
        expYear = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_year))
            )
        expYear.send_keys(year)

        # pay and confirm order
        pay_and_confirmBtn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_pay_and_confirm_order))
            )
        pay_and_confirmBtn.click()

    def orderPlaced(self):
        orderPlaced = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_orderPlaced))
            )
        return orderPlaced.text

    def download_and_continue(self):
        # download invoice
        downloadINV = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_download_invoice))
            )
        downloadINV.click()
        sleep(1)
        # continue for other shopping
        continueShopping = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_continue))
            )
        continueShopping.click()
