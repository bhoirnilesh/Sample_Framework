import pytest
from Utilities.LogUtils import cutomLoger
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import readConfig


class Test_001_Login:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = cutomLoger.get_logger()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("*************Test_0001_Login***************")
        self.logger.info("*************Verifying Home Page Title***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title =="JPetStore Demo":
            assert True
            self.driver.close()
            self.logger.info("*************Home Page Title test case passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.warn("*************Home Page Title test case failed ***************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************Verifying the Login test***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.gotoSignInPage()
        self.lp.clickOnSignIn()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        text =self.lp.getWelcomeText()
        if text.__contains__("Welcome"):
            assert True
            self.logger.info("*************Login test is passed***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("*************Login test is failed***************")
            assert False



