from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    enterStore_xpath = "//a[text()='Enter the Store']"
    clickOnsignIn_xpath = "//a[text()='Sign In']"
    textbox_username_xpath = "username"
    textbox_password_xpath = "password"
    button_login_xpath= "signon"
    signin_xpath = "//a[text()='Sign In']"
    signout_xpath = "//a[text()='Sign Out']"
    link_logout_linktext_xpath="Logout"
    welcome_text_xpath = "//div[@id='WelcomeContent']"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_xpath).clear()
        self.driver.find_element(By.NAME, self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_password_xpath).clear()
        self.driver.find_element(By.NAME, self.textbox_password_xpath).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.NAME,self.button_login_xpath).click()

    def getWelcomeText(self):
        return self.driver.find_element(By.XPATH, self.welcome_text_xpath).text

    def Logout(self):
        self.driver.find_element(By.XPATH, self.signout_xpath).click()

    def Signin(self):
        self.driver.find_element(By.XPATH, self.signin_xpath).click()

    def gotoSignInPage(self):
        self.driver.find_element(By.XPATH, self.enterStore_xpath).click()

    def clickOnSignIn(self):
        self.driver.find_element(By.XPATH, self.clickOnsignIn_xpath).click()