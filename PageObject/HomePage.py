from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.css_view_product = "a[href='/product_details/1']"
        self.id_quantity = "quantity"
        self.xpath_addToCart = "//button[normalize-space()='Add to cart']"
        self.xpath_continueShopping = "//button[normalize-space()='Continue Shopping']"
        self.xpath_view_cart = "//a[normalize-space()='Cart']"
        self.xpath_delete_fromCart = "//a[@class='cart_quantity_delete']"
        self.xpath_proceed_to_checkout = "//a[normalize-space()='Proceed To Checkout']"
        self.xpath_place_order = "//a[normalize-space()='Place Order']"

    def viewProduct(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(("css selector", self.css_view_product))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        viewProduct = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(("css selector", self.css_view_product))
        )
        viewProduct.click()

    def addQuantity(self, quantity):
        addQuantity = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("id", self.id_quantity))
            )
        addQuantity.send_keys(quantity)

    def addToCart_and_continue(self):
        addToCart = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_addToCart))
            )
        addToCart.click()
        sleep(1)
        continue_btn = self.driver.find_element("xpath", self.xpath_continueShopping)
        continue_btn.click()

    def viewCart(self):
        viewCart = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_view_cart))
            )
        viewCart.click()

    def proceedToCheckout(self):
        proceedToCheckout = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_proceed_to_checkout))
            )
        proceedToCheckout.click()

    def placeOrder(self):
        placeOrder = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(("xpath", self.xpath_place_order))
            )
        placeOrder.click()
