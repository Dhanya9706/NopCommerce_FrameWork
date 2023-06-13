from selenium import webdriver
import pytest


from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utillities.readProperties import ReadConfig
from utillities.customLogger import LogGen


class Test_001_Login():
    url=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()

    logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info('********************** test_homePageTitle ***************************')
        self.logger.info('********************** Verifying Home Page Title ***************************')

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        actual_title = self.driver.title
        print(actual_title)

        if actual_title=="Your store. Login":
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle1.png")
            self.driver.close()
            self.logger.info('********************** Test Passed ***************************')
            assert True
        else:
            self.logger.error('********************** Test Failed ***************************')
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_login(self,setup):

        self.logger.info('********************** Verifying Test Login ***************************')
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasswordName(self.password)
        self.lp.clickOnLogin()
        act_title=self.driver.title
        print(act_title)
        if act_title=="Dashboard / nopCommerce administration":
            self.driver.save_screenshot(".\\screenshots\\" + "test_login1.png")
            self.driver.close()
            self.logger.info('********************** Test Passed ***************************')
            assert True
        else:
            self.logger.error('********************** Test Failed ***************************')
            self.driver.close()
            assert False
