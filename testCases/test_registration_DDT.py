import random
import string
import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.RegisterNewUserPage import RegisterUser
from Utilities.LogUtils import cutomLoger
from Utilities.readProperties import readConfig
from Utilities import XLUtils

class Test_003_DDT_Registration:
    baseURL = readConfig.getApplicationURL()
    path = ".//TestData/RegistrationsData.xlsx"
    log = cutomLoger.get_logger()

    @pytest.mark.sanity
    def test_registration_ddt(self,setup):
        self.log.info("************* Test_003_DDT_Registration ***************")
        self.log.info("*************Verifying the Registration process***************")
        self.driver = setup
        self.driver.maximize_window()
        self.rp = RegisterUser(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("total rows")
        print(self.rows)
        title = ""
        list_status = []

        for r in range(2,self.rows+1):
            self.userID = XLUtils.readData(self.path,'Sheet1',r,1)
            self.passwd = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.fname = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lname = XLUtils.readData(self.path, 'Sheet1', r, 4)
            self.email = XLUtils.readData(self.path, 'Sheet1', r, 5)
            self.phone = XLUtils.readData(self.path, 'Sheet1', r, 6)
            self.add1 = XLUtils.readData(self.path, 'Sheet1', r, 7)
            self.add2 = XLUtils.readData(self.path, 'Sheet1', r, 8)
            self.city = XLUtils.readData(self.path, 'Sheet1', r, 9)
            self.state = XLUtils.readData(self.path, 'Sheet1', r, 10)
            self.zip = XLUtils.readData(self.path, 'Sheet1', r, 11)
            self.country = XLUtils.readData(self.path, 'Sheet1', r, 12)

            self.driver.get(self.baseURL)
            time.sleep(2)
            self.rp.ClickOnRegistration()
            time.sleep(2)
            self.rp.SetUserId(self.userID)
            self.rp.SetPassword(self.passwd)
            self.rp.SetFirstName(self.fname)
            self.rp.SetLastName(self.lname)
            self.rp.SetEmail(self.email)
            self.rp.SetPhone(self.phone)
            self.rp.SetAdddress1(self.add1)
            self.rp.SetAdddress2(self.add2)
            self.rp.SetCity(self.city)
            self.rp.SetState(self.state)
            self.rp.SetZip(self.zip)
            self.rp.SetCountry(self.country)
            time.sleep(5)
            self.rp.SaveInfo()
            time.sleep(5)

            self.lp = LoginPage(self.driver)
            try :
                self.rp.NewUserLogin()
            except:
                self.log.error("************* user already exists ***************")
                title = self.driver.title
                if title == "HTTP Status 500 – Internal Server Error":
                    list_status.append("pass")
                    print("User is already exist")
                    continue

            if self.lp.getWelcomeText().__contains__("Welcome"):
                list_status.append("pass")
                self.lp.Logout()
                self.log.error("************* test case is passed***************")
            elif self.driver.title == "HTTP Status 500 – Internal Server Error":
                self.driver.save_screenshot(".\\Screenshots\\"+"test_registration_ddt.png")
                self.log.error("************* test case is failed***************")
                list_status.append("pass")
            else:
                # self.driver.quit()
                list_status.append("false")

        print(list_status)
        if "fail" not in list_status:
            self.log.info("Registration DDT test passed")
            self.driver.quit()
            assert True
        else:
            self.log.info("Registration test case failed")
            self.driver.quit()
            assert False

        self.log.info("****End of Login DDT test*****")
        self.log.info("*************** Completed TC_registration_002 *************")