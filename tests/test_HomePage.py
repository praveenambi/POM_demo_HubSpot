from config.config import TestData
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORFD)
        title = homepage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert  title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORFD)
        header= homepage.get_header_value()
        assert  header == TestData.HOME_PAGE_HEADER


    def test_accountname_value(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORFD)
        accountname = homepage.get_accountname_value()
        assert  accountname == TestData.ACCOUNT_NAME

    def test_settings_iocn(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORFD)
        assert homepage.is_settings_icon_exist()

    def test_logout(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORFD)
        homepage.do_logout()










