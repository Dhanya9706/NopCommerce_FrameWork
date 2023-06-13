import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:

    linkcustomer_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p/i"
    link_customer_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    button_addnew_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    textbox_email_id="Email"
    textbox_password_id="Password"
    textbox_firstname_id="FirstName"
    textbox_lastname_id="LastName"
    radio_gendermale_id="Gender_Male"
    radio_genderfemale_id="Gender_Female"
    calen_dob_xpath="//*[@id='customer-info']/div[2]/div[6]/div[2]/span[1]/span/span/span"
    textbox_dob_id="DateOfBirth"
    textbox_company_id="Company"
    checkbox_taxexempt_id="IsTaxExempt"
    textbox_newsletter_xpath="//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div/input"
    textbox_newsyourstorename_xpath="//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    textbox_newsteststore2_xpath="//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    textbox_customerroles_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    textbox_cradministrator_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    textbox_crforum_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    textbox_crguest_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    textbox_crregistered_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    textbox_crvendor_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    checkbox_active_id="Active"
    textbox_admincomment_id="AdminComment"
    button_save_xpath="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"
    drpdown_vendor_id="VendorId"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,AddCustomer.linkcustomer_menu_xpath).click()

    def  clickOnCustomer(self):
        self.driver.find_element(By.XPATH,AddCustomer.link_customer_xpath).click()

    def addNewCustomer(self):
        self.driver.find_element(By.XPATH,AddCustomer.button_addnew_xpath).click()

    def setEmailId(self,email):
        self.driver.find_element(By.ID,AddCustomer.textbox_email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,AddCustomer.textbox_password_id).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.ID,AddCustomer.textbox_firstname_id).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.ID,AddCustomer.textbox_lastname_id).send_keys(lastname)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,AddCustomer.radio_gendermale_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,AddCustomer.radio_genderfemale_id).click()
        else:
            self.driver.find_element(By.ID, AddCustomer.radio_gendermale_id).click()

    def setDob(self,dob):
        self.driver.find_element(By.ID,AddCustomer.textbox_dob_id).send_keys(dob)

    def setCompanyName(self,company):
        self.driver.find_element(By.ID,AddCustomer.textbox_company_id).send_keys(company)

    def setTaxExemptTrue(self):
        self.driver.find_element(By.ID,AddCustomer.checkbox_taxexempt_id).click()

    def setActiveFalse(self):
        self.driver.find_element(By.ID,AddCustomer.checkbox_taxexempt_id).click()

    def addComment(self,commment):
        self.driver.find_element(By.ID,AddCustomer.textbox_admincomment_id).send_keys(commment)

    def saveCustomer(self):
        self.driver.find_element(By.XPATH,AddCustomer.button_save_xpath).click()

    def setvendor(self,vendor):
        vendor_option=Select(self.driver.find_element(By.ID,AddCustomer.drpdown_vendor_id))
        vendor_option.select_by_visible_text(vendor)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH,AddCustomer.textbox_customerroles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem=self.driver.find_element(By.XPATH,AddCustomer.textbox_crregistered_xpath)
        elif role == 'Adminstrators':
            self.listitem=self.driver.find_element(By.XPATH,AddCustomer.textbox_cradministrator_xpath)
        elif role == 'Forum Moderators':
            self.listitem=self.driver.find_element(By.XPATH,AddCustomer.textbox_crforum_xpath)
        elif role == 'guest':
            self.driver.find_element(By.XPATH,AddCustomer.textbox_crregistered_xpath).click()
            self.listitem=self.driver.find_element(By.XPATH,AddCustomer.textbox_crguest_xpath)
        elif role =='vendor':
            self.listitem=self.driver.find_element(By.XPATH,AddCustomer.textbox_crvendor_xpath)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();",self.listitem)


    def setNewsLetter(self,store):
        self.driver.find_element(By.XPATH,AddCustomer.textbox_newsletter_xpath).click()
        if store == 'Your store name':
            self.driver.find_element(By.XPATH,AddCustomer.textbox_newsyourstorename_xpath).click()
        elif store == 'Test store 2':
            self.driver.find_element(By.XPATH,AddCustomer.textbox_newsteststore2_xpath).click()




