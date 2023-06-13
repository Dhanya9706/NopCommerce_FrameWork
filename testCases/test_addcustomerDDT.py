import random
import string
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from pageObjects.AddCustomers import AddCustomer
from testCases import conftest
from utillities.customLogger import LogGen
from utillities.readProperties import ReadConfig
from utillities import XLUtils

class Test_003_AddCustomer():
    url=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def testAddCustomer(self,setup):
        self.logger.info("******************* Test_003_AddCustomer **************")
        self.logger.info("*************** Verify Add Customer **************** ")

        self.driver = setup
        self.driver.maximize_window()

        self.driver.get(Test_003_AddCustomer.url)

        self.logger.info("****************Login To Application****************")
        self.lg=Login(self.driver)
        self.lg.setUserName(Test_003_AddCustomer.username)
        self.lg.setPasswordName(Test_003_AddCustomer.password)
        self.lg.clickOnLogin()
        self.driver.save_screenshot(".\\screenshots\\"+"loginpage.png")
        self.logger.info("****************** Login Successful*******************")


        self.logger.info("****************** Starting Add Customer*********************")

        self.addcust = AddCustomer(self.driver)

        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomer()
        self.addcust.addNewCustomer()
        self.logger.info("*****************Adding customer info*******************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmailId(self.email)
        self.addcust.setPassword('Test123')
        self.addcust.setFirstName('Akshay')
        self.addcust.setLastName('Reddy')
        self.addcust.setGender('Female')
        self.addcust.setDob('1/12/2020')
        self.addcust.setCompanyName('Akshay Resturants')
        self.addcust.setTaxExemptTrue()
        time.sleep(3)
        self.addcust.setNewsLetter('Your store name')
        time.sleep(3)
        self.addcust.setCustomerRole('guest')
        self.addcust.setvendor('Vendor 1')
        self.addcust.addComment('Testing Practices')
        self.addcust.saveCustomer()

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text

        #print(self.msg)

        if 'customer has been added successfully.' in self.msg:
                #assert True
            self.logger.info("**************** Add Customer Test Passed *************")
            self.driver.save_screenshot(".\\screenshots\\"+"success.png")

        else:
                #assert False
            self.logger.info("***************** Add Customer Test Failed *********************")
            self.driver.save_screenshot(".\\screenshots\\"+"failure.png")

        self.driver.close()
        self.logger.info("******************* End Of Add Customer Test ********************")
def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))