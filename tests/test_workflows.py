import logging as log

import selenium
from appium.webdriver.common.touch_action import TouchAction
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

    # Selenium
    # web_driver = driver = webdriver.Chrome(executable_path='/Users/shelby/PycharmProjects/GeminiMobileUIAutomation/tests/chromedriver')

    @pytest.mark.end_to_end_test
    def login_water_prod_prod(self,driver,db):
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

        # assert int(ticket_number) == int(db_ticket_number)

        return ticket_number



    @pytest.mark.ticket_process
    def test_ticket_process(self,base_url,web_username,web_password,driver,db):

        ticket_number = self.login_water_prod_prod(driver,db)
        ticket_number = 786446

        username = "//input[@name='Email']"
        password = "//input[@name='Password']"
        login_button= "//*[span='Log in']"

        driver = webdriver.Chrome(executable_path='/Users/shelby/PycharmProjects/GeminiMobileUIAutomation/tests/chromedriver')

        driver.get(url="https://dev.geminishale.com")

        # login
        time.sleep(5)
        wait = WebDriverWait(driver, 90)
        wait.until(EC.element_to_be_clickable((By.XPATH, login_button)))
        email = driver.find_element(By.XPATH, "//input[@name='Email']")
        email.send_keys(web_username)

        password = driver.find_element(By.XPATH, password)
        password.send_keys(web_password)

        driver.find_element(By.XPATH, login_button).click()

        # Impersonate Hauler
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Service Providers']")))
        # gemini_menu = ".account-username"
        haulers = "//*[@data-icon='truck']"

        gemini_menu = driver.find_element(By.CLASS_NAME, "account-username")
        gemini_menu.click()

        wait.until(EC.element_to_be_clickable((By.XPATH, haulers)))
        haulers = driver.find_element(By.XPATH, haulers)
        haulers.click()
        #
        # Select Hauler
        impersonate_hauler_btn = "//span[text()='Impersonate Hauler']//parent::button"
        alert_box = "//h3[text()='Select a Hauler to impersonate']"
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selection-selected-value'])[2]")))
        driver.find_element(By.XPATH, "//div[@class='ant-select-lg ant-select ant-select-enabled']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@class='ant-select-search__field']").send_keys('U Call We Haul')
        # Hit The Enter key
        driver.find_element(By.XPATH, "//li[text()='U Call We Haul']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, impersonate_hauler_btn).click()
        time.sleep(1)

        # Tickets
        ticket_button = "//span[text()='Tickets ']"
        wait.until(EC.element_to_be_clickable((By.XPATH, ticket_button)))
        driver.find_element(By.XPATH, ticket_button).click()

        ticket_list = "//ul[@id='Tickets$Menu']//li[text()='Ticket List']"
        wait.until(EC.element_to_be_clickable((By.XPATH, ticket_list)))
        element = driver.find_element(By.XPATH, ticket_list)
        driver.execute_script("arguments[0].click();", element)

        # Find the ticket
        # search_icon = "//i[@class='anticon anticon-search ant-table-filter-icon ant-table-filter-open ant-dropdown-trigger ant-dropdown-open']//*[name()='svg']"
        search_icon = "//i[@title='Filter menu']//*[name()='svg']"
        add_new = "//button//span[text()='Add New']"
        wait.until(EC.element_to_be_clickable((By.XPATH, add_new)))
        time.sleep(5)
        ticket_number = f"(//td[text()='{ticket_number}'])[1]"

        element = driver.find_element(By.XPATH, ticket_number)
        driver.execute_script("arguments[0].click();", element)

        # Approve ticket as hauler
        approve_button = "button-text"
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, approve_button)))
        driver.find_element(By.CLASS_NAME, approve_button).click()

        # optional appprove pop up
        # A pop up if there is an issue occurs sometimes but not all the time
        # if else here
        time.sleep(1)
        approve = "//button//span[text()='Yes, approve']"
        if driver.find_element(By.XPATH,approve).is_displayed():
            element = driver.find_element(By.XPATH, approve)
            driver.execute_script("arguments[0].click();", element)

        # Assert here the ticket is now in operator review
        # wait.until(EC.element_to_be_clickable((By.XPATH, add_new)))
        time.sleep(5)
        element = driver.find_element(By.XPATH, ticket_number)
        wait.until(EC.element_to_be_clickable((By.XPATH, ticket_number)))
        driver.execute_script("arguments[0].click();", element)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Operator Review']")))
        operator_review = driver.find_element(By.XPATH, "//span[text()='Operator Review']")
        assert operator_review.is_displayed()

        # Close
        wait.until(EC.element_to_be_clickable((By.XPATH, ticket_number)))
        element = driver.find_element(By.XPATH, "//button[@class='ant-drawer-close']")
        driver.execute_script("arguments[0].click();", element)

        gemini_menu = driver.find_element(By.CLASS_NAME, "account-username")
        gemini_menu.click()
        # time.sleep(1)

        # Impersonate Operator
        operators = "//*[@data-icon='swords']//parent::li"
        wait.until(EC.element_to_be_clickable((By.XPATH, operators)))
        operators = driver.find_element(By.XPATH, operators)
        operators.click()
        time.sleep(1)

        alert_box_operators = "//h3[text()='Select an Operator to impersonate']"
        wait.until(EC.visibility_of_element_located((By.XPATH, alert_box_operators)))

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selection-selected-value'])[2]")))
        driver.find_element(By.XPATH, "//div[@class='ant-select-lg ant-select ant-select-enabled']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@class='ant-select-search ant-select-search--inline']/child::div/child::input").send_keys('Gemini Operations')
        # Hit The Enter key
        driver.find_element(By.XPATH, "//li[text()='Gemini Operations']").click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Impersonate Operator']//parent::button")))
        element = driver.find_element(By.XPATH, "//span[text()='Impersonate Operator']//parent::button")
        driver.execute_script("arguments[0].click();", element)


        # Operator Navigate to tickets
        time.sleep(1)
        # Tickets
        ticket_button = "//span[text()='Tickets ']"
        wait.until(EC.element_to_be_clickable((By.XPATH, ticket_button)))
        driver.find_element(By.XPATH, ticket_button).click()

        ticket_list = "//ul[@id='Tickets$Menu']//li[text()='Ticket List']"
        wait.until(EC.element_to_be_clickable((By.XPATH, ticket_list)))
        driver.find_element(By.XPATH, ticket_list).click()
        #
        # Find the ticket
        action_button = "//button[@class='ant-btn actions-btn ant-dropdown-trigger ant-btn-sm']"
        # wait.until(EC.element_to_be_clickable((By.XPATH, action_button)))
        time.sleep(5)

        element = driver.find_element(By.XPATH, ticket_number)
        driver.execute_script("arguments[0].click();", element)

        # Approve ticket as operator
        approve_button = "button-text"
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, approve_button)))
        driver.find_element(By.CLASS_NAME, approve_button).click()

        # optional appprove pop up
        # A pop up if there is an issue occurs sometimes but not all the time
        # if else here
        time.sleep(1)
        approve = "//button//span[text()='Yes, approve']"
        if driver.find_element(By.XPATH,approve).is_displayed():
            element = driver.find_element(By.XPATH, approve)
            driver.execute_script("arguments[0].click();", element)

        # Assert here the ticket is now in operator review
        time.sleep(5)
        # wait.until(EC.element_to_be_clickable((By.XPATH, ticket_number)))
        element = driver.find_element(By.XPATH, ticket_number)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        cost_assignment = driver.find_element(By.XPATH, "//span[text()='Cost Assignment']")
        assert cost_assignment.is_displayed()

        # Close
        driver.find_element(By.XPATH, "//button[@class='ant-drawer-close']").click()

        # Assignment of cost
        assignment_of_cost_option = "//span[text()='Assignment Of Cost']//parent::div//parent::li"
        wait.until(EC.element_to_be_clickable((By.XPATH, assignment_of_cost_option)))
        driver.find_element(By.XPATH, assignment_of_cost_option).click()


        # Now where to find that ticket?
        # This ticket was in production
        # You can get elements for the ul with the id of Assignment of Cost$Menu to go through all

        # # Click production
        production_option = "//span[text()='Production']//parent::li"
        wait.until(EC.element_to_be_clickable((By.XPATH, production_option)))
        driver.find_element(By.XPATH, production_option).click()
        #
        # Wait for the ticket to pop up
        "//span[text()='Actions']//parent::button"
        time.sleep(3)
        #
        # click on ticket
        driver.find_element(By.XPATH, ticket_number)
        element = driver.find_element(By.XPATH, "//span[text()='Actions']//parent::button")
        driver.execute_script("arguments[0].click();", element)

        # Click the ticket
        element = driver.find_element(By.XPATH, "//span[text()='Actions']//parent::button//parent::td")
        driver.execute_script("arguments[0].click();", element)
        #
        # Click assign at the top
        assign_button = "//span[text()='Assign']//parent::a"
        driver.find_element(By.XPATH, assign_button).click()

        # override if
        yes_override = "//span[text()='Yes, override']//parent::button"
        # if driver.find_element(By.XPATH, yes_override).is_displayed():
        element = driver.find_element(By.XPATH, yes_override)
        driver.execute_script("arguments[0].click();", element)

        #
        # assign
        time.sleep(2)
        # wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@title='Select an Account Area'])[1]")))
        account_area = "(//div[@title='Select an Account Area'])[1]"
        driver.find_element(By.XPATH, account_area).click()

        # Account area type
        all_options = driver.find_elements(By.XPATH, "//li[@role='option']")
        property_id = "//li[@role='option'][text()='Property ID']"
        billable_locations = "(//div[@class='ant-select-lg ant-select ant-select-enabled'])[1]"
        account_code = "(//div[@title='Select an Account Code']//parent::div)[1]"
        account_opt_220_040 = "//li[@role='option'][text()='220-040']"
        finish_button = "//span[text()='Finish']//parent::button"

        # assign account area
        driver.find_element(By.XPATH, property_id).click()
        time.sleep(1)

        # Billable locations
        driver.find_element(By.XPATH, billable_locations).click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//li[text()='CHAD GLAUSER-OHI-PAD1']").click()
        time.sleep(1)

        # Account Code
        driver.find_element(By.XPATH, account_code).click()
        driver.find_element(By.XPATH,account_opt_220_040).click()
        time.sleep(1)

        # Finish
        driver.find_element(By.XPATH, finish_button).click()
        time.sleep(2)

        # Go to assignment of cost
        assig_of_cost = "//span[text()='Assignment Of Cost']"
        driver.find_element(By.XPATH, assig_of_cost).click()


        # Go to cost awaiting review
        cost_awaiting_review = "//span[text()='Cost Awaiting Review']"
        element = driver.find_element(By.XPATH,cost_awaiting_review)
        driver.execute_script("arguments[0].click();", element)
        #
        # Production
        #
        production = "(//span[text()='Production']//parent::li)[2]"
        wait.until(EC.visibility_of_element_located((By.XPATH, production)))
        driver.find_element(By.XPATH, production).click()
        #
        # click on the ticket
        # no ticket number so just approve all
        production_tickets_buttons = "(//div[@class='ant-collapse-header'])[1]"
        wait.until(EC.element_to_be_clickable((By.XPATH, production_tickets_buttons)))
        driver.find_element(By.XPATH,production_tickets_buttons).click()
        #


















































