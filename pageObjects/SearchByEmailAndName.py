from selenium import webdriver
from selenium.webdriver.common.by import By

class Search:

    textbox_email_id="SearchEmail"
    textbox_firstname_id="SearchFirstName"
    button_search_id="search-customers"
    table_customer_id="customers-grid"
    table_rows_xpath="//table[@id='customers-grid']/tbody/tr"
    table_email_xpath="//table[@id='customers-grid']/tbody/tr/td[2]"
    table_name_xpath = "//table[@id='customers-grid']/tbody/tr/td[3]"

    def __init__(self,driver):
        self.driver = driver

    def setEmailId(self,email):
        self.driver.find_element(By.ID,Search.textbox_email_id).send_keys(email)

    def setFirstName(self,name):
        self.driver.find_element(By.ID,Search.textbox_firstname_id).send_keys(name)

    def clickOnSearch(self):
        self.driver.find_element(By.ID,Search.button_search_id).click()

    def getRowCount(self):
        self.count=self.driver.find_elements(By.XPATH,Search.table_rows_xpath)
        return len(self.count)

    def checkEmailId(self):
        return self.driver.find_element(By.XPATH,Search.table_email_xpath).text


    def checkFirstName(self):
        return self.driver.find_element(By.XPATH,Search.table_name_xpath).text