from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def setup(browser):
    if browser == 'chrome':
        serv_obj = Service("D:\\LatestChrome\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.implicitly_wait(10)
        print("Launching Chrome Browser")
        return driver
    else:
        serv_obj = Service("D:\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
        print("Launching Edge Browser")
        return driver


def pytest_addoption(parser): #This will get info frm CLI/hooks
    parser.addoption("--browser")

@pytest.fixture(scope="function")
def browser(request): #This will return browser value to set up method
    return request.config.getoption("--browser")


################To Add HTML Reports#######################

#It is the hook to add environment information to HTML report
def pytest_configure(config):
    config._metadata = {"Project Name" : 'NopCommerce',
    "Module Name" : 'Customer',
    "Tester" : 'Yashodha',}


#It is the hook th delete/modify environmental info to HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
