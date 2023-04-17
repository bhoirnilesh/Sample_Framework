from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RegisterUser:

    enterStore_xpath = "//a[text()='Enter the Store']"
    clickOnsignIn_xpath = "//a[text()='Sign In']"
    Registration_xpath = "//a[text()='Register Now!']"
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    repeated_password_xpath = "//input[@name='repeatedPassword']"
    firstName_xpath = "//input[@name='account.firstName']"
    lastName_xpath = "//input[@name='account.lastName']"
    email_xpath = "//input[@name='account.email']"
    phone_xpath = "//input[@name='account.phone']"
    address1_xpath = "//input[@name='account.address1']"
    address2_xpath = "//input[@name='account.address2']"
    city_xpath = "//input[@name='account.city']"
    state_xpath = "//input[@name='account.state']"
    zip_xpath = "//input[@name='account.zip']"
    country_xpath = "//input[@name='account.country']"
    saveAccountInfo_xpath = "//input[@value='Save Account Information']"
    UID  = ""
    PWD = ""
    login_button_xpath = "//input[@value='Login']"


    def __init__(self,driver):
        self.driver=driver

    def ClickOnRegistration(self):
        self.driver.find_element(By.XPATH, self.enterStore_xpath).click()
        self.driver.find_element(By.XPATH, self.clickOnsignIn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Registration_xpath).click()

    def SetUserId(self,userID):
        self.UID = userID
        self.driver.find_element(By.XPATH, self.username_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(userID)

    def SetPassword(self, password):
        self.PWD = password
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.repeated_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.repeated_password_xpath).send_keys(password)

    def SetFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.firstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstName_xpath).send_keys(firstname)

    def SetLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.lastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.lastName_xpath).send_keys(lastname)


    def SetEmail(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def SetPhone(self, phone):
        self.driver.find_element(By.XPATH, self.phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.phone_xpath).send_keys(phone)

    def SetAdddress1(self, address1):
        self.driver.find_element(By.XPATH, self.address1_xpath).clear()
        self.driver.find_element(By.XPATH, self.address1_xpath).send_keys(address1)

    def SetAdddress2(self, address2):
        self.driver.find_element(By.XPATH, self.address2_xpath).clear()
        self.driver.find_element(By.XPATH, self.address2_xpath).send_keys(address2)

    def SetCity(self, city):
        self.driver.find_element(By.XPATH, self.city_xpath).clear()
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(city)

    def SetState(self, state):
        self.driver.find_element(By.XPATH, self.state_xpath).clear()
        self.driver.find_element(By.XPATH, self.state_xpath).send_keys(state)

    def SetZip(self, zip):
        self.driver.find_element(By.XPATH, self.zip_xpath).clear()
        self.driver.find_element(By.XPATH, self.zip_xpath).send_keys(zip)

    def SetCountry(self, country):
        self.driver.find_element(By.XPATH, self.country_xpath).clear()
        self.driver.find_element(By.XPATH, self.country_xpath).send_keys(country)

    def SaveInfo(self):
        self.driver.find_element(By.XPATH, self.saveAccountInfo_xpath).click()

    def NewUserLogin(self):
        self.driver.find_element(By.XPATH, self.clickOnsignIn_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.username_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(self.UID)
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(self.PWD)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()





