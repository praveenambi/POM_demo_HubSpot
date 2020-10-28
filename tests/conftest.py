import pytest
from selenium import webdriver  # import the webdriver from selenium
from webdriver_manager.chrome import ChromeDriverManager  # import the chrome Driver manager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"],scope='class')    # run only in chrome
def init_driver(request):
    if request.param =="chrome":
        wb_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param =="IE":
       wb_driver =  webdriver.Ie(executable_path=IEDriverManager().install())
    request.cls.driver = wb_driver
    yield
    wb_driver.close()