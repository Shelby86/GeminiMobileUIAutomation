import logging as log

import selenium
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from helpers.db_helpers import DBHelper

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

    ticket_button_element = "//android.widget.TextView[@text = 'Ticket']"
    pull_volume_element = "//android.widget.EditText[@text='Enter or pull volume']"
    ok_button_pop_up_element = "//android.widget.TextView[@text = 'Okay']"
    source_field_element = "//android.widget.TextView[@text = 'Select a source for pick-up']"
    adams_1_element = "//android.widget.TextView[@text ='ADAMS 1 (BUCKEYE BRINE, LLC)']"
    intended_destination_drop_off_element = "//android.widget.TextView[@text = 'Select a destination for drop-off']"
    adams_2_element = "//android.widget.TextView[@text='ADAMS 2 (BUCKEYE BRINE, LLC)']"

    ticket_number_element = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]"
    complete_pickup_button_element = "//android.widget.TextView[@text = 'Complete pick-up']"

    ticket_element = "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"

    complete_drop_off_button_element = "//android.widget.TextView[@text = 'Complete drop-off']"
    completed_button_element = "//android.widget.TextView[@text = 'COMPLETED']"

    ticket_full_path = "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView"
    pull_volume_full_xpath = "//android.view.ViewGroup[3]/android.widget.EditText"

    back_button_full_x_path = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup"
    menu_full_xpath = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup"
    log_out_full_xpath = "//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]"
    completed_full_xpath = "//android.view.View[2]/android.view.ViewGroup"

    # We have to wait for an element to be clickable
    # There are no locators on the clickable elements

    @pytest.mark.end_to_end_test
    def test_login_water_prod_prod(self,driver,db):
        wait = WebDriverWait(driver, 90)
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.EditText[@text = "Username"]')))

        # login
        driver.find_element(By.XPATH,self.username_el).send_keys("geminiworktests+ucallwehaul@gmail.com")
        driver.find_element(By.XPATH, self.password_el).send_keys("H@uling2")
        driver.find_element(By.XPATH, self.login_button_el).click()

        # select truck
        wait.until(EC.element_to_be_clickable((By.XPATH, self.truck_el)))
        driver.find_element(By.XPATH, self.truck_el).click()
        #
        wait.until(EC.element_to_be_clickable((By.XPATH, self.truck_selection_el)))
        ticket_number = driver.find_element(By.XPATH, self.truck_selection_el).click()
        print(ticket_number)

        # select operator
        wait.until(EC.element_to_be_clickable((By.XPATH, self.operator_el)))
        driver.find_element(By.XPATH, self.operator_el).click()
        #
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

        try:
            driver.find_element(By.XPATH, self.production_el).click()
            time.sleep(3)
        except:selenium.common.exceptions
        else: TouchAction(driver).tap(None, 555, 231, 1).perform()
        finally:TouchAction(driver).tap(None, 555, 231, 1).perform()

        next_button.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, self.production_production_el)))
        driver.find_element(By.XPATH, self.production_production_el).click()
        next_button.click()

        # Verify login
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, self.ticket_full_path)))
        except: selenium.common.exceptions.StaleElementReferenceException
        else: wait.until(EC.element_to_be_clickable((By.XPATH, self.ticket_full_path)))

        # ticket
        time.sleep(5)
        # try:
        driver.find_element(By.XPATH, self.ticket_button_element).click()
        # except: selenium.common.exceptions.StaleElementReferenceException
        # else: TouchAction(driver).tap(None, 197, 1248, 1).perform()

        # pull volume
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.pull_volume_element)))
            driver.find_element(By.XPATH, self.pull_volume_element).click()
            time.sleep(3)
        except:selenium.common.exceptions.NoSuchElementException
        # 368, 726
        else: TouchAction(driver).tap(None, 450, 736, 2).perform()
        finally: TouchAction(driver).tap(None, 450, 736, 2).perform()

        # accept alert
        wait.until(EC.visibility_of_element_located((By.XPATH, self.okay_el)))
        driver.find_element(By.XPATH, self.okay_el).click()

        # pull volume
        wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@text='Enter or pull volume']")))
        driver.find_element(By.XPATH, self.pull_volume_element).click()
        driver.find_element(By.XPATH, self.pull_volume_element).send_keys(60)

        # Source
        wait.until(EC.visibility_of_element_located((By.XPATH, self.source_field_element)))
        driver.find_element(By.XPATH, self.source_field_element).click()

        # Source Location
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.adams_1_element)))
            time.sleep(3)
        except:selenium.common.exceptions
        else: TouchAction(driver).tap(None, 782, 394, 1).perform()
        finally: TouchAction(driver).tap(None, 782, 394, 1).perform()

        # destination
        wait.until(EC.visibility_of_element_located((By.XPATH, self.intended_destination_drop_off_element)))
        driver.find_element(By.XPATH, self.intended_destination_drop_off_element).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, self.adams_2_element)))
        driver.find_element(By.XPATH, self.adams_2_element).click()

        # Complete pick up
        wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Complete pick-up']")))
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='Complete pick-up']").click()

        # get the ticket number
        source_on_ticket = "//android.widget.TextView[@text='Source: ']"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Source: ']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='Source: ']").click()
        #
        wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]")))
        ticket_number = driver.find_element(By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]").text
        print(ticket_number)

        # click ticket to complete drop off
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Source: ']")))
            driver.find_element(By.XPATH, "//android.widget.TextView[@text='Source: ']").click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Source: ']")))
        except: selenium.common.exceptions.NoSuchElementException
        # 500, 1115
        else: TouchAction(driver).tap(None, 768, 226, 1).perform()
        # finally: TouchAction(driver).tap(None, 768, 226, 1).perform()

        # drop off
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.complete_drop_off_button_element)))
            driver.find_element(By.XPATH,self.complete_drop_off_button_element).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, self.complete_drop_off_button_element)))
        except: selenium.common.exceptions.NoSuchElementException
        # 500, 1115
        else: TouchAction(driver).tap(None, 500, 1115, 1).perform()
        finally: TouchAction(driver).tap(None, 500, 1115, 2).perform()

        # Go to Completed
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='COMPLETED']")))
            driver.find_element(By.XPATH, "//android.widget.TextView[@text='COMPLETED']").click()
            time.sleep(3)
        except: selenium.common.exceptions.NoSuchElementException
        # 500, 1115
        else: TouchAction(driver).tap(None, 437, 134, 1).perform()
        finally: TouchAction(driver).tap(None, 437, 134, 1).perform()

        # Click on the ticket
        wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Source: ']")))
        completed_ticket_number = driver.find_element(By.XPATH, "//android.view.ViewGroup[1]/android.widget.TextView[2]").text
        wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup")))
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='Source: ']").click()

        # verify
        wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Update drop-off']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='Update drop-off']").is_displayed()

        assert ticket_number == completed_ticket_number

        # log out
        driver.find_element(By.XPATH, self.back_button_full_x_path).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.menu_full_xpath)))
        driver.find_element(By.XPATH, self.menu_full_xpath).click()

        time.sleep(5)
        TouchAction(driver).tap(None, 660, 1141, 2).perform()

        wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.EditText[@text = "Username"]')))
        driver.find_element(By.XPATH, '//android.widget.EditText[@text = "Username"]').is_displayed()

        driver.quit()

        # Verify  in the DB
        sql = f"""SELECT [Id]
      ,[TicketId]
      ,[LoadTypeId]
      ,[SourceWellPadId]
      ,[SourceVolume]
      ,[IntendedDestinationOutletId]
      ,[DestinationTankId]
      ,[Rerouted]
      ,[TicketStatusId]
      ,[Enabled]
  FROM [audit].[Ticket]
  WHERE 
  TicketId = {ticket_number}"""

        db_ticket = DBHelper.query_runner_as_dict(db,query=sql)
        print(db_ticket)
        db_ticket_number = db_ticket['results'][0]['TicketId']

        assert ticket_number == db_ticket_number

        # Now start the selenium





