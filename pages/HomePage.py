from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage


class HomePage(BasePage):
    HEADER = (By.XPATH,'//i18n-string[text()="User Guide"]')
    ACCOUNT_NAME = (By.XPATH, '//span[@class="account-name "]')
    SETTING_ICON = (By.ID, 'navSetting')
    SIGN_OUT_LINK = (By.ID, 'signout')

    def __init__(self,driver):
        self.driver= driver
        super.__init__(driver)


    def get_home_page_title(self,title):
        return  self.get_title(title)

    def is_settings_icon_exist(self):
        return  self.is_visible(self.SETTING_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return  self.get_element_text(self.HEADER)

    def get_accountname_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return  self.get_element_text(self.ACCOUNT_NAME)


    def do_logout(self):
        self.do_click(self.ACCOUNT_NAME)
        self.do_click(self.SIGN_OUT_LINK)
        return  LoginPage(self.driver)


