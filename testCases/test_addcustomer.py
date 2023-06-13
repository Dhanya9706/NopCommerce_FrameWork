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

    @pytest.mark.regression
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
        self.path="D:\\Project\\NopCommerce_FrameWork\\testData\\addcustomerinput.xlsx"

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print(self.rows)

        for r in range(2,self.rows+1):

            self.addcust.addNewCustomer()
            self.logger.info("*****************Adding customer info*******************")

            #self.email = random_generator() + "@gmail.com"
            self.addcust.setEmailId(XLUtils.readData(self.path,'Sheet1',r,1))
            self.addcust.setPassword(XLUtils.readData(self.path,'Sheet1',r,2))
            self.addcust.setFirstName(XLUtils.readData(self.path,'Sheet1',r,3))
            self.addcust.setLastName(XLUtils.readData(self.path,'Sheet1',r,4))
            self.addcust.setGender(XLUtils.readData(self.path,'Sheet1',r,5))
            self.addcust.setDob(XLUtils.readData(self.path,'Sheet1',r,6))
            self.addcust.setCompanyName(XLUtils.readData(self.path,'Sheet1',r,7))
            self.tax=XLUtils.readData(self.path,'Sheet1',r,8)
            if(self.tax == 1):
                self.addcust.setTaxExemptTrue()
            time.sleep(3)
            self.addcust.setNewsLetter(XLUtils.readData(self.path,'Sheet1',r,9))
            time.sleep(3)
            self.addcust.setCustomerRole(XLUtils.readData(self.path,'Sheet1',r,10))
            self.addcust.setvendor(XLUtils.readData(self.path,'Sheet1',r,11))
            self.addcust.addComment(XLUtils.readData(self.path,'Sheet1',r,12))
            self.addcust.saveCustomer()

            self.msg=self.driver.find_element(By.TAG_NAME,"body").text

            #print(self.msg)

            if 'customer has been added successfully.' in self.msg:
                #assert True
                self.logger.info("**************** Add Customer Test Passed *************")
                self.driver.save_screenshot(".\\screenshots\\"+"success.png")
                XLUtils.writeData(self.path,'Sheet1',r,13,'Pass')
                XLUtils.fillGreenColour(self.path,'Sheet1',r,13)
            else:
                #assert False
                self.logger.info("***************** Add Customer Test Failed *********************")
                self.driver.save_screenshot(".\\screenshots\\"+"failure.png")
                XLUtils.writeData(self.path, 'Sheet1', r, 13, 'Fail')
                XLUtils.fillRedColour(self.path, 'Sheet1', r, 13)

        self.driver.close()
        self.logger.info("******************* End Of Add Customer Test ********************")


def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))