import logging as log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


class Login:


    @staticmethod
    def login(driver):
        username_el = "//android.widget.EditText[@text = 'Username']"
        password_el = "//android.widget.EditText[@text = 'Password']"
        login_button_el = "//android.widget.TextView[@text = 'Login']"
        truck_el = "//android.widget.TextView[@text = 'Select the truck you are driving today']"
        truck_selection_el = "//android.widget.TextView[@text = 'Haul5']"
        operator_el = "//android.widget.TextView[@text = 'Select the Operator you are hauling for']"
        operator_selection_el = "//android.widget.TextView[@text = 'Gemini Operations']"
        next_button_el = "//android.widget.TextView[@text = 'Next']"
        water_el = "//android.widget.TextView[@text = 'Water']"
        production_el = "//android.widget.TextView[@text='Production']"
        production_production_el = "//android.widget.TextView[@text = 'Production-Production']"
        ticket_button_el = "//android.widget.TextView[@text = 'Ticket']"

        wait = WebDriverWait(driver, 50)
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.EditText[@text = "Username"]')))

        # login
        driver.find_element(By.XPATH,username_el).send_keys("geminiworktests+ucallwehaul@gmail.com")
        driver.find_element(By.XPATH,password_el).send_keys("H@uling2")
        driver.find_element(By.XPATH,login_button_el).click()

        # select truck
        wait.until(EC.element_to_be_clickable((By.XPATH,truck_el)))
        driver.find_element(By.XPATH,truck_el).click()

        wait.until(EC.element_to_be_clickable((By.XPATH,truck_selection_el)))
        driver.find_element(By.XPATH,truck_selection_el).click()

        # select operator
        wait.until(EC.visibility_of_element_located((By.XPATH,operator_el)))
        driver.find_element(By.XPATH,operator_el).click()

        wait.until(EC.visibility_of_element_located((By.XPATH,operator_selection_el)))
        driver.find_element(By.XPATH,operator_selection_el).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,next_button_el)))

        # workflow
        next_button = driver.find_element(By.XPATH,next_button_el)
        next_button.click()

        wait.until(EC.visibility_of_element_located((By.XPATH,water_el)))
        driver.find_element(By.XPATH, water_el).click()
        next_button.click()


        wait.until(EC.element_to_be_clickable((By.XPATH,production_el)))
        driver.find_element(By.XPATH,production_el).click()
        next_button.click()

        wait.until(EC.visibility_of_element_located((By.XPATH,production_production_el)))
        driver.find_element(By.XPATH,production_production_el).click()
        next_button.click()

        # Verify login
        wait.until(EC.visibility_of_element_located((By.XPATH,ticket_button_el)))
