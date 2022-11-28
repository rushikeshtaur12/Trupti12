import pytest
from selenium import webdriver
from LIBRARY.config import Config
import time


#CROSS BROWSING

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["Chrome","Firefox","Edge"])
def _driver(request):
    if request.param=="Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param=="Firefox":
        options= Options()
        options.binary_location=r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path,options=options)
    elif request.param=="Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    ###########################################################
    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    print(driver.title)
    driver.save_screenshot("booking_1.png")
    driver.close()
    ##########################################################







