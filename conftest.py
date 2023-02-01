import pytest
import os
import time
import pyodbc
from webdriver_manager.chrome import ChromeDriverManager
#


from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.testproject.sdk.drivers import webdriver
import time
from selenium.webdriver.support.select import Select
import os



@pytest.fixture()
def driver():
    os.environ['TP_DEV_TOKEN'] = 'cjxMY8F-KjBPguVLNQdfMflpi8EPlWz1hw_2OUsyohU1'
    desired_capabilities = {
        "appWaitDuration": 60000,
        "appActivity": "org.geminishalesolutions.gemini.MainActivity",
        "appPackage": 'org.geminishalesolutions.gemini.dev',
        "platformName": "Android",
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        "version": 11,
        "launchTimeout": 60000,
        "idleTimeout": 600,
        "appWaitPackage": "org.geminishalesolutions.gemini.dev",
        # "autoLaunch": False
    }

    driver = webdriver.Remote(desired_capabilities=desired_capabilities)
    driver.start_activity(app_package='org.geminishalesolutions.gemini.dev',
                          app_activity='org.geminishalesolutions.gemini.MainActivity')

    return driver

@pytest.fixture()
def db():
    server = 'geminishaledev01.database.windows.net'
    database = 'GeminiShale'
    username = 'Automation'
    password = '0lIvquRHSRe2cvYkNiFG'
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';ENCRYPT=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    return cursor

@pytest.fixture()
def wait():
    x = WebDriverWait(driver, 50)
    return x


@pytest.fixture()
def username():
    return "geminiworktests+ucallwehaul@gmail.com"


@pytest.fixture()
def password():
    return "H@uling2"

@pytest.fixture()
def base_url():
    return "https://dev.geminishale.com"


@pytest.fixture()
def web_username():
    return 'shelby.nester@geminishale.com'


@pytest.fixture()
def web_password():
    return 'W0rk3rB33!'