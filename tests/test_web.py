from set_up.mobile_set_up import MobileSetUp
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from src.testproject.sdk.drivers.actions.action_guids import actions

from helpers.db_helpers import DBHelper
from tests.base import Base
from selenium.webdriver.common.keys import Keys

class TestWeb:

    def test_approve_ticket(self,username,password,db,driver):
        ticket_number = MobileSetUp.simple_ticket(self,driver,username,password)

        username = "//input[@name='Email']"
        password = "//input[@name='Password']"
        login_button = "//*[span='Log in']"

        driver = webdriver.Chrome(
            executable_path='/Users/shelby/PycharmProjects/GeminiMobileUIAutomation/tests/chromedriver')

        driver.get(url="https://dev.geminishale.com")