import  pytest

from config.config import TestData
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class Test_login(BaseTest):

    def test_signup_link_visible(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_sinupLink_exist()
        assert flag


    def test_loginpage_title(self):
        self.loginpage = LoginPage(self.driver)
        tittle =  self.loginpage.get_title(TestData.PAGE_TITLE)
        assert  tittle == TestData.PAGE_TITLE

    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME,TestData.PASSWORFD)
