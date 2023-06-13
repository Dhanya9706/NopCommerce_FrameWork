import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from webdriver_manager import driver

from utillities.readProperties import ReadConfig
from pageObjects.LoginPage import Login
from utillities.customLogger import LogGen
from utillities import XLUtils


class Test002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/Input_login.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**************************Test_002_login_ddt test**********************")
        self.driver = setup
        #self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("number of rows in Excel:", self.rows)
        # empty list variable
        list_status=[]

        for r in range(2,self.rows+1):

            self.driver.get(self.baseURL)
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPasswordName(self.password)
            self.lp.clickOnLogin()
            time.sleep(10)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***test pass***")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                    XLUtils.writeData(self.path,'Sheet1',r,4,'Pass')
                    XLUtils.fillGreenColour(self.path,'Sheet1',r,4)
                    self.driver.save_screenshot(".\\screenshots\\"+"TestCase "+self.user+".png")
                elif self.exp == 'fail':
                    self.logger.info("***test failed***")
                    self.lp.clickLogout();
                    list_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, 'fail')
                    XLUtils.fillRedColour(self.path, 'Sheet1', r, 4)
                    self.driver.save_screenshot(".\\screenshots\\" + "TestCase " + self.user + ".png")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***test failed***")
                    list_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, 'fail')
                    XLUtils.fillRedColour(self.path, 'Sheet1', r, 4)
                    self.driver.save_screenshot(".\\screenshots\\" + "TestCase " + self.user + ".png")
                elif self.exp == 'fail':
                    self.logger.info("***passed***")
                    list_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, 'Pass')
                    XLUtils.fillGreenColour(self.path, 'Sheet1', r, 4)

                    self.driver.save_screenshot(".\\screenshots\\" + "TestCase " + self.user + ".png")
            print(list_status)
        if "Fail" not in list_status:
            self.logger.info("********Login ddt test passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********Login ddt test failed*********")
            self.driver.close()
            assert False
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")
