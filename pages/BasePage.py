from selenium import webdriver  # import the webdriver from selenium
from selenium.webdriver.common.by import By   # import  the By class from selenium
import time  #import the time class

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager  # import the chrome Driver manager
from webdriver_manager.firefox import GeckoDriverManager  # import the geckodriver manager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
# Install the WebDriver manager by terminal by command "pip install webdriver-manager"

""" This is the base page and super class of all classes"""
""""It contains all the genaric functions and utilities for all the pages """


class BasePage:
    def __init__(self,driver):
        self.driver=driver


    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def do_send_Keys(self,by_locator,text):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return  element.text

    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_is(title))
        return  self.driver.title













