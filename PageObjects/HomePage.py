from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    fish_xpath = "//img[contains(@src,'fish_icon.gif')]"
    dogs_xpath = "//img[contains(@src,'dogs_icon.gif')]"
    cats_xpath = "//img[contains(@src,'cats_icon.gif')]"
    reptiles_xpath = "//img[contains(@src,'reptiles_icon.gif')]"
    birds_xpath = "//img[contains(@src,'birds_icon.gif')]"
    Animal_list = "//td"


    def __init__(self,driver):
        self.driver=driver

    def ClickOnFish(self):
        self.driver.find_element(By.XPATH,self.fish_xpath).click()

    def ClickOnDogs(self):
        self.driver.find_element(By.XPATH, self.dogs_xpath).click()

    def ClickOnCats(self):
        self.driver.find_element(By.XPATH,self.cats_xpath).click()

    def ClickOnReptiles(self):
        self.driver.find_element(By.XPATH,self.reptiles_xpath).click()

    def ClickOnBirds(self):
        self.driver.find_element(By.XPATH,self.birds_xpath).click()
