import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class TestWorkflows:

    username_el = "//android.widget.EditText[@text = 'Username']"
    password_el = "//android.widget.EditText[@text = 'Password']"
    login_button_el =  "//android.widget.TextView[@text = 'Login']"
    truck_el = "//android.widget.TextView[@text = 'Select the truck you are driving today']"
    truck_selection_el = "//android.widget.TextView[@text = 'Haul5']"
    operator_el = "//android.widget.TextView[@text = 'Select the Operator you are hauling for']"
    operator_selection_el = "//android.widget.TextView[@text = 'Gemini Operations']"
    next_button_el = "//android.widget.TextView[@text = 'Next']"
    water_el = "//android.widget.TextView[@text = 'Water']"
    production_el = "//android.widget.TextView[@text='Production']"
    production_production_el = "//android.widget.TextView[@text = 'Production-Production']"
    ticket_button_el = "//android.widget.TextView[@text = 'Ticket']"

    pull_volume_el = "//android.widget.EditText[@text = 'Enter or pull volume']"
    okay_el = "//android.widget.TextView[@text = 'Okay']"
    source_el = "//android.widget.TextView[@text = 'Select a source for pick-up']"
    source_option_el = "//android.widget.TextView[@text = 'ADAMS 1 (BUCKEYE BRINE, LLC)']"
    destination_el = "//android.widget.TextView[@text = 'Select a destination for drop-off']"
    intended_destination_el = "//android.widget.TextView[@text='ADAMS 2 (BUCKEYE BRINE, LLC)']"
    complete_pickup_el = "//android.widget.TextView[@text = 'Complete pick-up']"
    ticket_el = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]"
    complete_pickup_el = "//android.widget.TextView[@text = 'Complete pick-up']"
    ticket_text = "//android.widget.TextView[@text='Ticket #:']"
    line_tht_has_the_ticket_number = "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]"
    full_ticket_number_xpath = "//android.view.ViewGroup[1]/android.widget.TextView[2]"
    drop_off_el = "//android.widget.TextView[@text = 'Complete drop-off']"



    @pytest.mark.login_water_prod_prod
    def test_login_water_prod_prod(self,driver):
        wait = WebDriverWait(driver, 50)
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.EditText[@text = "Username"]')))

        # login
        driver.find_element(By.XPATH,self.username_el).send_keys("geminiworktests+ucallwehaul@gmail.com")
        driver.find_element(By.XPATH, self.password_el).send_keys("H@uling2")
        driver.find_element(By.XPATH, self.login_button_el).click()

        # select truck
        wait.until(EC.element_to_be_clickable((By.XPATH, self.truck_el)))
        driver.find_element(By.XPATH, self.truck_el).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, self.truck_selection_el)))
        driver.find_element(By.XPATH, self.truck_selection_el).click()

        # select operator
        wait.until(EC.visibility_of_element_located((By.XPATH, self.operator_el)))
        driver.find_element(By.XPATH, self.operator_el).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, self.operator_selection_el)))
        driver.find_element(By.XPATH, self.operator_selection_el).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.next_button_el)))

        # workflow
        next_button = driver.find_element(By.XPATH, self.next_button_el)
        next_button.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, self.water_el)))
        driver.find_element(By.XPATH, self.water_el).click()
        next_button.click()


        wait.until(EC.element_to_be_clickable((By.XPATH, self.production_el)))
        driver.find_element(By.XPATH, self.production_el).click()
        next_button.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, self.production_production_el)))
        driver.find_element(By.XPATH, self.production_production_el).click()
        next_button.click()

        # Verify login
        wait.until(EC.visibility_of_element_located((By.XPATH, self.ticket_button_el)))

        driver.quit()

    @pytest.mark.simple_ticket
    def test_simple_ticket_no_login(self,driver,db,wait):
        time.sleep(10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.ticket_button_el)))
        ticket_button = driver.find_element(By.XPATH, self.ticket_button_el)
        ticket_button.click()

        # Wait for ticket
        wait.until(EC.visibility_of_element_located((By.XPATH, self.source_el)))

        #
        pull_volume = driver.find_element(By.XPATH, self.pull_volume_el)
        pull_volume.click()

        #
        driver.find_element(By.XPATH, self.okay_el).click()

        #
        wait.until(EC.visibility_of_element_located((By.XPATH, self.ticket_button_el)))
        pull_volume.click()
        pull_volume.send_keys(55)

        #
        source = driver.find_element(By.XPATH, self.source_el)
        source.click()

        #
        wait.until(EC.visibility_of_element_located((By.XPATH, self.source_option_el)))
        driver.find_element(By.XPATH, self.source_option_el).click()

        #
        driver.find_element(By.XPATH, self.destination_el).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, self.intended_destination_el)))
        driver.find_element(By.XPATH, self.intended_destination_el).click()

        #
        driver.find_element(By.XPATH, self.complete_pickup_el).click()

        #
        wait.until(EC.visibility_of_element_located((By.XPATH, self.ticket_el)))
        ticket_number = driver.find_element(By.XPATH, self.line_tht_has_the_ticket_number).get_text()
        driver.find_element(By.XPATH, self.ticket_text).click()

        #
        wait.until(EC.visibility_of_element_located((By.XPATH, self.destination_el)))
        driver.find_element(By.XPATH, self.drop_off_el).click()

        print(ticket_number)
        logging.info(ticket_number)


# Adams 1 to Addelman A
# End at Addelman A



