# from time import sleep
# import logging as logger
# from PageObject.AccountInfo import AccInfo
# from PageObject.AddressInfo import AddInfo
# from PageObject.LogIn_or_SignUp_Page import LogInorSignUp
# import pytest
# import configparser
#
# parser = configparser.ConfigParser()
# parser.read("Utilities/input.properties")
#
# @pytest.mark.usefixtures("page")
# class Test_login:
#     def setup(self):
#         # valid credentials
#         self.login = LogInorSignUp(self.driver)
#         self.email_id = parser.get("LogIn_credential", "lemailID")
#         self.password = parser.get("LogIn_credential", "passwordL")
#
#         # invalid credentials
#         self.wremail_id = parser.get("Wrong_LogIn_credential", "wrlemailID")
#         self.wrpassword = parser.get("Wrong_LogIn_credential", "wrasswordL")
#
#         self.name = parser.get("SignUp_credential", "name")
#         self.semailID = parser.get("SignUp_credential", "semailID")
#         self.firstname = parser.get("SignUp_credential", "firstname")
#         self.lastname = parser.get("SignUp_credential", "lastname")
#         self.company = parser.get("SignUp_credential", "company")
#         self.address = parser.get("SignUp_credential", "address")
#         self.state = parser.get("SignUp_credential", "state")
#         self.city = parser.get("SignUp_credential", "city")
#         self.zipCode = parser.get("SignUp_credential", "zipCode")
#         self.mobileNo = parser.get("SignUp_credential", "mobileNo")
#
#     def test_login(self):
#         logIsignUp = LogInorSignUp(self.driver)
#         accInfo = AccInfo(self.driver)
#         addInfo = AddInfo(self.driver)
#         logIsignUp.signIn_logIn()
#         logIsignUp.inputName(self.name)
#         logIsignUp.inputEmailId(self.semailID)
#         logIsignUp.signIn_btn()
#         sleep(3)
#
#         if "Email Address already exist!" in logIsignUp.exist_account():
#             logIsignUp.logIn_mailI_and_password(self.email_id, self.password)
#             logIsignUp.logIn_btn()
#             sleep(3)
#             logIsignUp.quite_logIn()
#
#         else:
#             if "ENTER ACCOUNT INFORMATION" in accInfo.check_title():
#                 assert True, logger.info("Title get matched")
#             else:
#                 assert False, logger.info("Title get matched")
#
#             accInfo.select_gender()
#             accInfo.input_password(parser.get("SignUp_credential", "passwordS"))
#             accInfo.date_of_birth()
#             sleep(2)
#             if "ADDRESS INFORMATION" == addInfo.check_title():
#                 assert True, logger.info("Title get matched")
#             else:
#                 assert False, logger.info("Title get matched")
#
#             addInfo.fullName(self.firstname, self.lastname)
#             sleep(1)
#
#             addInfo.companyName_with_address(self.company, self.address)
#             addInfo.select_country()
#             sleep(2)
#
#             addInfo.state_and_city_name(self.state, self.city)
#             sleep(1)
#
#             addInfo.zipCode_and_mobileNo(self.zipCode, self.mobileNo)
#             addInfo.createAcc_btn()
#             if "ACCOUNT CREATED!" == addInfo.check_msg():
#                 assert True, logger.info("Title get matched")
#             else:
#                 assert False, logger.info("Title get matched")
#             sleep(3)
#             addInfo.click_continue()
#
#     def test_login_wrongInput(self):
#         logIsignUp = LogInorSignUp(self.driver)
#         logIsignUp.signIn_logIn()
#         logIsignUp.logIn_mailI_and_password(self.wremail_id, self.wrpassword)
#         logIsignUp.logIn_btn()
#

from time import sleep
import logging as logger

from PageObject.AccountInfo import AccInfo
from PageObject.AddressInfo import AddInfo
from PageObject.LogIn_or_SignUp_Page import LogIn_or_SignUp
from PageObject.HomePage import HomePage
from PageObject.PaymentDetails import PaymentDetails
import pytest
import configparser

parser = configparser.ConfigParser()
parser.read("Utilities/input.properties")


@pytest.mark.usefixtures("page")
class Test_login:
    # Define class-level variables for credentials
    # valid credentials
    email_id = parser.get("LogIn_credential", "emailIDL")
    password = parser.get("LogIn_credential", "passwordL")
    # invalid credentials
    email_idWR = parser.get("Wrong_LogIn_credential", "emailIDWRL")
    passwordWR = parser.get("Wrong_LogIn_credential", "passwordWRL")

    name = parser.get("SignUp_credential", "name")
    emailIDS = parser.get("SignUp_credential", "emailIDS")
    firstname = parser.get("SignUp_credential", "firstname")
    lastname = parser.get("SignUp_credential", "lastname")
    company = parser.get("SignUp_credential", "company")
    address = parser.get("SignUp_credential", "address")
    state = parser.get("SignUp_credential", "state")
    city = parser.get("SignUp_credential", "city")
    zipCode = parser.get("SignUp_credential", "zipCode")
    mobileNo = parser.get("SignUp_credential", "mobileNo")

    # homePage parser
    quantity = parser.get("HP_Detail", "quantity")
    namePD = parser.get("PD_Detail", "namePD")
    cardNumber = parser.get("PD_Detail", "cardNo")
    cvcNumber = parser.get("PD_Detail", "cvcNo")
    monthPD = parser.get("PD_Detail", "month")
    yearPD = parser.get("PD_Detail", "year")

    def setup(self):
        # valid credentials
        self.login = LogIn_or_SignUp(self.driver)

    def test_login(self):
        logIsignUp = LogIn_or_SignUp(self.driver)
        accInfo = AccInfo(self.driver)
        addInfo = AddInfo(self.driver)
        logIsignUp.signIn_logIn()
        logIsignUp.inputName(Test_login.name)
        sleep(1)
        logIsignUp.inputEmailId(Test_login.emailIDS)
        sleep(1)
        logIsignUp.signIn_btn()
        sleep(3)

        exist_text = logIsignUp.exist_account()
        if exist_text is not None and "Email Address already exist!" in exist_text:
            logIsignUp.logIn_mailI_and_password(Test_login.email_id, Test_login.password)
            logIsignUp.logIn_btn()
            sleep(3)
            logIsignUp.quite_logIn()
        else:
            if "ENTER ACCOUNT INFORMATION" in accInfo.check_title():
                assert True, logger.info("Title get matched")
            else:
                assert False, logger.info("Title get matched")

            accInfo.select_gender()
            accInfo.input_password(parser.get("SignUp_credential", "passwordS"))
            accInfo.date_of_birth()
            sleep(2)
            if "ADDRESS INFORMATION" == addInfo.check_title():
                assert True, logger.info("Title get matched")
            else:
                assert False, logger.info("Title get matched")

            addInfo.fullName(Test_login.firstname, Test_login.lastname)
            sleep(1)

            addInfo.companyName_with_address(Test_login.company, Test_login.address)
            addInfo.select_country()
            sleep(2)

            addInfo.state_and_city_name(Test_login.state, Test_login.city)
            sleep(1)

            addInfo.zipCode_and_mobileNo(Test_login.zipCode, Test_login.mobileNo)
            addInfo.createAcc_btn()
            if "ACCOUNT CREATED!" == addInfo.check_msg():
                assert True, logger.info("Title get matched")
            else:
                assert False, logger.info("Title get matched")
            sleep(3)
            addInfo.click_continue()

    def test_login_wrongInput(self):
        logIsignUp = LogIn_or_SignUp(self.driver)
        logIsignUp.signIn_logIn()
        logIsignUp.logIn_mailI_and_password(Test_login.email_idWR, Test_login.passwordWR)
        logIsignUp.logIn_btn()

    def test_addToCart_and_placedOrder(self):
        logIsignUp = LogIn_or_SignUp(self.driver)
        homePage = HomePage(self.driver)
        paymentDet = PaymentDetails(self.driver)
        logIsignUp.signIn_logIn()
        logIsignUp.logIn_mailI_and_password(Test_login.email_id, Test_login.password)
        logIsignUp.logIn_btn()
        sleep(1)
        homePage.viewProduct()
        sleep(1)
        homePage.addQuantity(Test_login.quantity)
        sleep(1)
        homePage.addToCart_and_continue()
        sleep(1)
        homePage.viewCart()
        sleep(1)
        homePage.proceedToCheckout()
        sleep(1)
        homePage.placeOrder()
        sleep(1)
        paymentDet.name_and_cardDetails(Test_login.namePD, Test_login.cardNumber, Test_login.cvcNumber, Test_login.monthPD, Test_login.yearPD)
        sleep(1)
        paymentDet.orderPlaced()
        sleep(1)
        paymentDet.download_and_continue()
        sleep(3)
