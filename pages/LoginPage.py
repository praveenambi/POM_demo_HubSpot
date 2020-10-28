from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage
from pages.HomePage import HomePage


class LoginPage(BasePage):
    ''' By locators - object repositery'''

    EMAIL_ID = (By.ID,'username')
    PASSWORD = (By.ID,'password')
    LOGIN_BUTTON =  (By.ID, 'loginBtn')
    SIGNUP_LINK =  (By.LINK_TEXT,'Sign up')


    ''' constructor of the page class  , calling super class constructor'''
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    ''' Page axtions for login page   '''

    ''' This is used to get the page title'''
    def get_loginPage_title(self,title):
        return  self.get_title(title)

    ''' This methos id used to check the sing up link n login page'''
    def is_sinupLink_exist(self):
        return  self.is_visible(self.SIGNUP_LINK)

    ''' This method is used to perform the login action'''
    def do_login(self,username,password):
        self.do_send_Keys(self.EMAIL_ID,username)
        self.do_send_Keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)












