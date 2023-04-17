import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.LogUtils import cutomLoger
from Utilities.readProperties import readConfig
from Utilities import XLUtils
class Test_002_DDT_Login:
    baseURL = readConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    log = cutomLoger.get_logger()

    def test_login_ddt(self, setup):
        self.log.info("************* Test_002_DDT_Login ***************")
        self.log.info("*************Verifying the Login test***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.gotoSignInPage()
        self.lp.Signin()
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print(self.rows)
        list_status=[]        #Empty list variable

        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(1)
            self.log.info("Validating username:"+self.username+ "password:"+self.password)
            try:
                text = self.lp.getWelcomeText()
            except :
                text = "none"
            # if text.__contains__("Welcome"):
            #     self.log.info("*************** Log in successfull **************")
            #     self.log.info("User is valid")
            #     self.log.info("Username : "+self.username)
            #     self.log.info("Password : "+ self.password)
            #     list_status.append("Pass")
            #     self.lp.Logout()
            #     time.sleep(2)
            #     self.lp.Signin()
            #     self.log.info("*********************************************************")
            # else:
            #     self.log.info("***************** Log in unsuccessful *******************")
            #     self.log.info("Invalid username or password")
            #     list_status.append("Pass")

            if text.__contains__("Welcome"):
                if self.exp == 'pass':
                    self.log.info("************* Login Successful ***************")
                    print("************* Login test is passed ***************")
                    list_status.append("Pass")
                    self.lp.Logout()
                    time.sleep(2)
                    self.lp.Signin()
                    self.log.info("*************** User is valid *******************")
                    continue
                elif self.exp == 'fail':
                    list_status.append('Fail')
                    self.log.info("*************** Login test failed *******************")
                    time.sleep(2)
                    continue
            else :
                if self.exp == 'pass':
                    self.log.info("************* Login test is passed ***************")
                    list_status.append("Pass")
                    self.log.info("*************** User is invalid *******************")
                    time.sleep(2)
                    continue
                elif self.exp == 'fail':
                    self.log.info("************* passed ***************")
                    list_status.append('Pass')
                    time.sleep(2)
                    continue

        print(list_status)
        if "Fail" not  in list_status:
            self.log.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.log.info("Login DDT test case failed")
            self.driver.close()
            assert False

        self.log.info("****End of Login DDT test*****")
        self.log.info("*************** Completed TC_LoginDDT_002 *************")


