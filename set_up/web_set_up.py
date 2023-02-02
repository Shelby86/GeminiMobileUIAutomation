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

class WebSetUp:
    username = "//input[@name='Email']"
    password = "//input[@name='Password']"
    login_button = "//*[span='Log in']"

    gemini_menu = "account-username"
    imp_service_provider = "//span[text()='Service Providers']"
    imp_haulers = "//*[@data-icon='truck']"

    # impersonate popup box
    hauler_popup_box = "//h3[text()='Select a Hauler to impersonate']"
    impersonate_hauler_btn = "//span[text()='Impersonate Hauler']//parent::button"
    pop_up_box_select_menu = "(//div[@class='ant-select-selection-selected-value'])[2]"
    pop_up_box_select_drop_down_clicked = "//div[@class='ant-select-lg ant-select ant-select-enabled']"
    pop_up_input_field = "//input[@class='ant-select-search__field']"

    def web_login(self,web_username,web_password,base_url):
        driver = webdriver.Chrome(
            executable_path='/Users/shelby/PycharmProjects/GeminiMobileUIAutomation/tests/chromedriver')

        driver.get(url=base_url)

        # login
        time.sleep(5)
        wait = WebDriverWait(driver, 90)
        wait.until(EC.element_to_be_clickable((By.XPATH, login_button)))
        email = driver.find_element(By.XPATH, username)
        email.send_keys(web_username)

        password = driver.find_element(By.XPATH, password)
        password.send_keys(web_password)

        driver.find_element(By.XPATH, login_button).click()


    def impersonate_hauler(self):
        driver = webdriver.Chrome(
            executable_path='/Users/shelby/PycharmProjects/GeminiMobileUIAutomation/tests/chromedriver')
        wait = WebDriverWait(driver, 90)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, gemini_menu)))

        gemini_menu = driver.find_element(By.CLASS_NAME, gemini_menu)
        gemini_menu.click()

        wait.until(EC.element_to_be_clickable((By.XPATH, imp_haulers)))
        haulers = driver.find_element(By.XPATH, imp_haulers)
        haulers.click()

        hauler = "U Call We Haul'"

        # Select Hauler
        wait.until(EC.element_to_be_clickable((By.XPATH, pop_up_box_select_menu)))
        driver.find_element(By.XPATH, pop_up_box_select_drop_down_clicked).click()
        time.sleep(3)
        driver.find_element(By.XPATH, pop_up_input_field).send_keys(hauler)
        # Hit The Enter key
        driver.find_element(By.XPATH, f"//li[text()='{hauler}']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, impersonate_hauler_btn).click()
        time.sleep(5)
