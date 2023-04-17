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
    path = ".//TestData/RegistrationData.xlsx"
    log = cutomLoger.get_logger()

    @pytest.mark.regression
    def test_registration_random(self,setup):
        self.log.info("************* Test_003_DDT_Registration ***************")
        self.log.info("*************Verifying the Registration process***************")
        self.driver = setup
        self.rp = RegisterUser(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        # print(self.rows)
        list_status = []
        # list_userData = {}


        random_userId = "user" + random_generator()
        random_email = random_generator()+"@abc.com.invalid"
        print(random_userId)

        # for r in range(5,self.rows+1):
        #     self.userID = XLUtils.readData(self.path,'Sheet1',r,1)
        #     self.passwd = XLUtils.readData(self.path, 'Sheet1', r, 2)
        #     self.fname = XLUtils.readData(self.path, 'Sheet1', r, 3)
        #     self.lname = XLUtils.readData(self.path, 'Sheet1', r, 4)
        #     self.email = XLUtils.readData(self.path, 'Sheet1', r, 5)
        #     self.phone = XLUtils.readData(self.path, 'Sheet1', r, 6)
        #     self.add1 = XLUtils.readData(self.path, 'Sheet1', r, 7)
        #     self.add2 = XLUtils.readData(self.path, 'Sheet1', r, 8)
        #     self.city = XLUtils.readData(self.path, 'Sheet1', r, 9)
        #     self.state = XLUtils.readData(self.path, 'Sheet1', r, 10)
        #     self.zip = XLUtils.readData(self.path, 'Sheet1', r, 11)
        #     self.country = XLUtils.readData(self.path, 'Sheet1', r, 12)

        self.driver.get(self.baseURL)
        time.sleep(2)
        self.rp.ClickOnRegistration()
        time.sleep(2)
        self.rp.SetUserId(random_userId)
        self.rp.SetPassword("password123")
        self.rp.SetFirstName("fname")
        self.rp.SetLastName("lname")
        self.rp.SetEmail(random_email)
        self.rp.SetPhone("09987000098")
        self.rp.SetAdddress1("add1")
        self.rp.SetAdddress2("add2")
        self.rp.SetCity("Delhi")
        self.rp.SetState("MH")
        self.rp.SetZip("23455")
        self.rp.SetCountry("India")
        time.sleep(5)
        self.rp.SaveInfo()
        time.sleep(5)

        self.lp = LoginPage(self.driver)
        try :
            self.rp.NewUserLogin()
            print(self.driver.title)
            print(self.driver.current_url)
            text = self.lp.getWelcomeText()
        except:
            self.log.error("************* user already exists ***************")
            list_status.append("pass")
            text="none"

        if text.__contains__("Welcome"):
            list_status.append("pass")
            self.lp.Logout()
            self.log.error("************* test case is passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_registration_ddt.png")
            self.log.error("************* test case is failed***************")
            list_status.append("fail")
            # self.driver.quit()
            # assert False

        print(list_status)
        if "fail" not in list_status:
            self.log.info("Registration DDT test passed")
            self.driver.quit()
            assert True
        else:
            self.log.info("Login DDT test case failed")
            self.driver.quit()
            assert False

        self.log.info("****End of Login DDT test*****")
        self.log.info("*************** Completed TC_LoginDDT_002 *************")

        with open("autogenratedusers.txt", "a") as fw:
            fw.write("\nusername = " + random_userId+"   ")
            fw.write("Password = " + "password" +"  ")
            fw.write("email =" + random_email+"")


def random_generator(size=5, chars=string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars) for x in range(size))