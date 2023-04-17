from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AnimalList:

    Animal = "(//td)[1]"
    add_toCart = "(//a[text()='Add to Cart'])[1]"
    proceedToCheckout = "//a[text()='Proceed to Checkout']"
    Continue = "//input[@value='Continue']"
    confirm = "//a[text()='Confirm']"
    ReturnMainMenu = "//a[text()='Return to Main Menu']"
    purchase_status = "//li[text()='Thank you, your order has been submitted.']"

    def __init__(self,driver):
        self.driver=driver

    # def getAnimalList(self,username):
    #     animal_list = self.driver.find_elements(By.XPATH,self.Animal_list)
    #     return animal_list

    def purchasePet(self):
        self.driver.find_element(By.XPATH, self.Animal).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.add_toCart).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.proceedToCheckout).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Continue).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.confirm).click()
        time.sleep(2)
        status = self.driver.find_element(By.XPATH, self.purchase_status).is_displayed()
        return status
        #     return status
        # for animal in animal_list:
        #     if animal.text == Animal_name:
        #         animal.click()
        #         break

    # def AddToCart(self):
    #     self.driver.find_element(By.XPATH,self.add_toCart).click()
    #
    # def ProceedToCheckout(self):
    #     self.driver.find_element(By.XPATH, self.proceedToCheckout).click()
    #
    # def ClickOnContinue(self):
    #     self.driver.find_element(By.XPATH, self.Continue).click()
    #
    # def ClickOnConfirm(self):
    #     self.driver.find_element(By.XPATH, self.confirm).click()
    #
    def ReturnToMainMenu(self):
        self.driver.find_element(By.XPATH, self.ReturnMainMenu).click()

    # def CheckPurchaseStatus(self):
    #     status = self.driver.find_element(By.XPATH, self.purchase_status).isDisplayed()
    #     return status