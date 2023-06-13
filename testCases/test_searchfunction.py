import time
import pytest
from selenium import webdriver

from pageObjects.LoginPage import Login
from pageObjects.AddCustomers import AddCustomer
from pageObjects.SearchByEmailAndName import Search
from utillities.customLogger import LogGen
from utillities.readProperties import ReadConfig
from utillities import XLUtils

class Test_004_searchfunction():
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmailId()
    firstname = ReadConfig.getFirstName()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def testSearchFunctionByEmail(self,setup):
        Test_004_searchfunction.logger.info("**************** Test 004 Search Function *******************")
        Test_004_searchfunction.logger.info("*************** Test Search Function By Email ********************")

        Test_004_searchfunction.logger.info("**************** Login to application ******************")
        self.driver = setup

        self.driver.get(Test_004_searchfunction.url)
        self.driver.maximize_window()

        self.lg = Login(self.driver)

        self.lg.setUserName(Test_004_searchfunction.username)
        self.lg.setPasswordName(Test_004_searchfunction.password)
        self.lg.clickOnLogin()

        Test_004_searchfunction.logger.info("******************* Navigating to customers *******************")

        self.addcust = AddCustomer(self.driver)

        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomer()

        Test_004_searchfunction.logger.info("******************** Search By Email ID *******************")

        self.searchf = Search(self.driver)

        self.searchf.setEmailId(Test_004_searchfunction.email)
        self.searchf.clickOnSearch()

        time.sleep(3)

        if self.searchf.checkEmailId() == Test_004_searchfunction.email and self.searchf.getRowCount() == 1:
            Test_004_searchfunction.logger.info("**************** Search By Email is Passed*****************")
            assert True
        else:
            Test_004_searchfunction.logger.info("**************** Search By Email is Failed*****************")
            assert False

        self.driver.close()

    @pytest.mark.regression
    def testSearchFunctionByName(self,setup):
        Test_004_searchfunction.logger.info("**************** Test 004 Search Function *******************")
        Test_004_searchfunction.logger.info("*************** Test Search Function By Name ********************")

        Test_004_searchfunction.logger.info("**************** Login to application ******************")
        self.driver = setup

        self.driver.get(Test_004_searchfunction.url)
        self.driver.maximize_window()

        self.lg = Login(self.driver)

        self.lg.setUserName(Test_004_searchfunction.username)
        self.lg.setPasswordName(Test_004_searchfunction.password)
        self.lg.clickOnLogin()

        Test_004_searchfunction.logger.info("******************* Navigating to customers *******************")

        self.addcust = AddCustomer(self.driver)

        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomer()

        Test_004_searchfunction.logger.info("******************** Search By Name *******************")

        self.searchf = Search(self.driver)

        self.searchf.setFirstName(Test_004_searchfunction.firstname)
        self.searchf.clickOnSearch()

        time.sleep(3)

        if Test_004_searchfunction.firstname in self.searchf.checkFirstName() and self.searchf.getRowCount() == 1:
            Test_004_searchfunction.logger.info("**************** Search By Name is Passed*****************")
            assert True
        else:
            Test_004_searchfunction.logger.info("**************** Search By Name is Failed*****************")
            assert False

        self.driver.close()