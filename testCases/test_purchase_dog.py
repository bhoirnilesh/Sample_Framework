import time

import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.LogUtils import cutomLoger
from Utilities.readProperties import readConfig
from PageObjects.HomePage import HomePage
from PageObjects.AnimalsListPage import AnimalList

class Test_001_Login:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    log = cutomLoger.get_logger()


    @pytest.mark.regression
    def test_purchase_dog(self, setup):
        self.log.info("*************Verifying the purchase dog test 001***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.gotoSignInPage()
        self.lp.Signin()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        text = self.lp.getWelcomeText()
        if text.__contains__("Welcome"):
            self.log.info("************* test is passed***************")
            self.hp = HomePage(self.driver)
            self.AnimalList = AnimalList(self.driver)
            self.hp.ClickOnDogs()
            status = self.AnimalList.purchasePet()
            if status == True:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\test_purchase_dog.png")
                self.AnimalList.ReturnToMainMenu()
                assert True
                self.driver.close()
            else:
                self.driver.close()
                assert False

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.log.error("************* test is failed***************")
            assert False

    @pytest.mark.sanity
    def test_purchase_cat(self, setup):
        self.log.info("*************Verifying the purchase for Cat test_002***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.gotoSignInPage()
        self.lp.Signin()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        text = self.lp.getWelcomeText()
        if text.__contains__("Welcome"):
            self.log.info("*************Login test is passed***************")
            self.hp = HomePage(self.driver)
            self.AnimalList = AnimalList(self.driver)
            self.hp.ClickOnCats()
            status = self.AnimalList.purchasePet()
            if status == True:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\test_purchase_dog.png")
                self.AnimalList.ReturnToMainMenu()
                assert True
                self.driver.close()
            else:
                self.driver.close()
                assert False

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.log.error("*************Login test is failed***************")
            assert False


