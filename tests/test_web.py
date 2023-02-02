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
from set_up.web_set_up import WebSetUp
from helpers.db_helpers import DBHelper
from tests.base import Base
from selenium.webdriver.common.keys import Keys

class TestWeb:
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

    pull_volume_el = "//android.widget.EditText[@text = 'Enter or pull volume']"
    okay_el = "//android.widget.TextView[@text = 'Okay']"
    source_el = "//android.widget.TextView[@text = 'Select a source for pick-up']"
    source_option_el = "//android.widget.TextView[@text = 'ADAMS 1 (BUCKEYE BRINE, LLC)']"
    destination_el = "//android.widget.TextView[@text = 'Select a destination for drop-off']"
    intended_destination_el = "//android.widget.TextView[@text='ADAMS 2 (BUCKEYE BRINE, LLC)']"
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

    complete_drop_off_button_element = "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]"
    completed_button_element = "//android.widget.TextView[@text = 'COMPLETED']"

    ticket_full_path = "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView"
    pull_volume_full_xpath = "//android.view.ViewGroup[3]/android.widget.EditText"

    back_button_full_x_path = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup"
    menu_full_xpath = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup"
    log_out_full_xpath = "//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]"
    completed_full_xpath = "//android.view.View[2]/android.view.ViewGroup"
    username = "//input[@name='Email']"
    password = "//input[@name='Password']"
    login_button = "//*[span='Log in']"

    gemini_menu = "account-username"
    imp_service_provider = "//span[text()='Service Providers']"
    imp_haulers = "//*[@data-icon='truck']"
    imp_operator = "//*[@data-icon='swords']//parent::li"

    # impersonate popup box
    hauler_popup_box = "//h3[text()='Select a Hauler to impersonate']"
    operator_pop_up_box = "//h3[text()='Select an Operator to impersonate']"
    impersonate_hauler_btn = "//span[text()='Impersonate Hauler']//parent::button"
    impersonate_operator_btn = "//span[text()='Impersonate Operator']//parent::button"
    pop_up_box_select_menu = "(//div[@class='ant-select-selection-selected-value'])[2]"
    pop_up_box_select_drop_down_clicked = "//div[@class='ant-select-lg ant-select ant-select-enabled']"
    pop_up_input_field = "//input[@class='ant-select-search__field']"

    # Dashboard for Hauler/Operator
    tickets_dropdown = "//span[text()='Tickets ']"

    # Ticket dropdown options
    ticket_list = "//ul[@id='Tickets$Menu']//li[text()='Ticket List']"

    # Ticket grid for self dispatch
    add_new = "//button//span[text()='Add New']"

    # Ticket options
    approve_button = "button-text"
    close_button = "//button[@class='ant-drawer-close']"

    # Ticket issue pop up box
    yes_approve = "//button//span[text()='Yes, approve']"

    # Assignment of cost
    assignment_of_cost_option = "//span[text()='Assignment Of Cost']//parent::div//parent::li"

    # Assignment of Cost Options
    production = "//span[text()='Production']//parent::li"

    # Assignment of cost ticket grid
    actions_button = "//span[text()='Actions']//parent::button"
    ticket_row = "//span[text()='Actions']//parent::button//parent::td"
    assign_button = "//span[text()='Assign']//parent::a"
    yes_override_btn = "//span[text()='Yes, override']//parent::button"

    # assignment of cost options
    account_area = "(//div[@title='Select an Account Area'])[1]"
    # Account area type
    all_options = "//li[@role='option']"
    property_id = "//li[@role='option'][text()='Property ID']"
    billable_locations = "(//div[@class='ant-select-lg ant-select ant-select-enabled'])[1]"
    account_code = "(//div[@title='Select an Account Code']//parent::div)[1]"
    account_opt_220_040 = "//li[@role='option'][text()='220-040']"
    finish_button = "//span[text()='Finish']//parent::button"

    # Cost awainting review
    cost_awaiting_review = "//span[text()='Cost Awaiting Review']"

    @pytest.mark.approve_ticket_2
    def test_approve_ticket(self,username,password,db,driver,web_username,web_password,base_url):
        ticket_number = MobileSetUp.simple_ticket(self,driver,username,password)
        # ticket_number = 786507
        ticket_number = f"(//td[text()='{ticket_number}'])[1]"

        # # login
        driver = webdriver.Chrome(
            executable_path='/Users/shelby/PycharmProjects/GeminiMobileUIAutomation/tests/chromedriver')
        driver.get(url=base_url)

        time.sleep(5)
        wait = WebDriverWait(driver, 90)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
        email = driver.find_element(By.XPATH, self.username)
        email.send_keys(web_username)
        password = driver.find_element(By.XPATH, self.password)
        password.send_keys(web_password)
        driver.find_element(By.XPATH, self.login_button).click()

        # Click Gemini Menu
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.gemini_menu)))
        gemini_menu = driver.find_element(By.CLASS_NAME,self.gemini_menu)
        gemini_menu.click()

        # Impersonate a Hauler
        wait.until(EC.element_to_be_clickable((By.XPATH, self.imp_haulers)))
        haulers = driver.find_element(By.XPATH, self.imp_haulers)
        haulers.click()

        # Select Hauler
        hauler = "U Call We Haul"
        wait.until(EC.element_to_be_clickable((By.XPATH, self.pop_up_box_select_menu)))
        driver.find_element(By.XPATH, self.pop_up_box_select_drop_down_clicked).click()
        time.sleep(3)
        driver.find_element(By.XPATH, self.pop_up_input_field).send_keys(hauler)
        # Hit The Enter key
        driver.find_element(By.XPATH, f"//li[text()='{hauler}']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, self.impersonate_hauler_btn).click()
        time.sleep(1)

        # Go to Hauler Tickets
        wait.until(EC.element_to_be_clickable((By.XPATH, self.tickets_dropdown)))
        driver.find_element(By.XPATH, self.tickets_dropdown).click()

        # Select ticket lists
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.ticket_list)))
        element = driver.find_element(By.XPATH, self.ticket_list)
        driver.execute_script("arguments[0].click();", element)

        # Find the ticket
        # wait.until(EC.element_to_be_clickable((By.XPATH, self.add_new)))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Tickets']")))
        time.sleep(6)
        element = driver.find_element(By.XPATH, ticket_number)
        driver.execute_script("arguments[0].click();", element)

        # Approve ticket as hauler
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.approve_button)))
        driver.find_element(By.CLASS_NAME, self.approve_button).click()

        # optional approve pop up
        # A pop up if there is an issue occurs sometimes but not all the time
        # if else here
        time.sleep(1)
        if driver.find_element(By.XPATH, self.yes_approve).is_displayed():
            element = driver.find_element(By.XPATH, self.yes_approve)
            driver.execute_script("arguments[0].click();", element)

        # Assert here the ticket is now in operator review
        time.sleep(3)
        element = driver.find_element(By.XPATH, ticket_number)
        wait.until(EC.element_to_be_clickable((By.XPATH, ticket_number)))
        driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Operator Review']")))
        operator_review = driver.find_element(By.XPATH, "//span[text()='Operator Review']")
        assert operator_review.is_displayed()

        # Close
        wait.until(EC.element_to_be_clickable((By.XPATH, ticket_number)))
        element = driver.find_element(By.XPATH, self.close_button)
        driver.execute_script("arguments[0].click();", element)

        # Click Gemini Menu
        time.sleep(10)
        e = driver.find_element_by_id("accountNav")
        location = e.location
        size = e.size
        w, h = size['width'], size['height']
        driver.find_element(By.ID, "accountNav").click()
        time.sleep(3)
        # Impersonate an Operator
        driver.find_element_by_xpath("(//*[text()='Operators']//parent::li)[2]").click()

        # Select Operator
        operator = "Gemini Operations"
        "//div[@class='ant-select-lg ant-select ant-select-enabled']"
        wait.until(EC.element_to_be_clickable((By.XPATH, self.pop_up_box_select_menu)))
        driver.find_element(By.XPATH, self.pop_up_box_select_drop_down_clicked).click()
        time.sleep(3)
        # driver.find_element(By.XPATH, "//*[text()='Select']").send_keys(operator)
        # Hit The Enter key
        driver.find_element(By.XPATH, f"//li[text()='{operator}']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, self.impersonate_operator_btn).click()
        time.sleep(1)

        # Go to operators tickets
        wait.until(EC.element_to_be_clickable((By.XPATH, self.tickets_dropdown)))
        driver.find_element(By.XPATH, self.tickets_dropdown).click()

        # Select Ticket Lists
        wait.until(EC.element_to_be_clickable((By.XPATH, self.ticket_list)))
        element = driver.find_element(By.XPATH, self.ticket_list)
        driver.execute_script("arguments[0].click();", element)

        # Find the ticket
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@title='Filter menu']")))
        time.sleep(6)
        element = driver.find_element(By.XPATH, ticket_number)
        driver.execute_script("arguments[0].click();", element)

        # Approve the ticket as Operator
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.approve_button)))
        driver.find_element(By.CLASS_NAME, self.approve_button).click()

        # optional approve pop up
        # A pop up if there is an issue occurs sometimes but not all the time
        time.sleep(1)
        if driver.find_element(By.XPATH, self.yes_approve).is_displayed():
            element = driver.find_element(By.XPATH, self.yes_approve)
            driver.execute_script("arguments[0].click();", element)

        # Assert ticket is in Cost Assignment
        time.sleep(10)
        element = driver.find_element(By.XPATH, ticket_number)
        driver.execute_script("arguments[0].click();", element)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Cost Assignment']//parent::div")))
        time.sleep(3)
        driver.find_element(By.XPATH, self.close_button).click()

        # Go to Assignment of Cost
        wait.until(EC.element_to_be_clickable((By.XPATH, self.assignment_of_cost_option)))
        driver.find_element(By.XPATH, self.assignment_of_cost_option).click()

        # Select Production
        wait.until(EC.element_to_be_clickable((By.XPATH, self.production)))
        driver.find_element(By.XPATH, self.production).click()

        # Find the ticket
        wait.until(EC.visibility_of_element_located((By.XPATH, ticket_number)))
        driver.find_element(By.XPATH, ticket_number)
        element = driver.find_element(By.XPATH, self.actions_button)
        driver.execute_script("arguments[0].click();", element)

        # Click the ticket
        element = driver.find_element(By.XPATH, self.ticket_row)
        driver.execute_script("arguments[0].click();", element)

        # Click assign at the top
        driver.find_element(By.XPATH, self.assign_button).click()

        # optional approve pop up
        # A pop up if there is an issue occurs sometimes but not all the time
        time.sleep(1)
        if driver.find_element(By.XPATH, self.yes_override_btn).is_displayed():
            element = driver.find_element(By.XPATH, self.yes_override_btn)
            driver.execute_script("arguments[0].click();", element)

        # Assignment of cost ticket
        time.sleep(2)
        driver.find_element(By.XPATH, self.account_area).click()

        # assignment of cost area
        driver.find_element(By.XPATH, self.property_id).click()
        time.sleep(1)

        # Billable locations
        driver.find_element(By.XPATH, self.billable_locations).click()
        time.sleep(6)
        driver.find_element(By.XPATH, "//li[text()='CHAD GLAUSER-OHI-PAD1']").click()
        time.sleep(1)

        # Account Code
        driver.find_element(By.XPATH, self.account_code).click()
        driver.find_element(By.XPATH, self.account_opt_220_040).click()
        time.sleep(1)

        # Finish
        driver.find_element(By.XPATH, self.finish_button).click()
        time.sleep(2)

        # Verify Ticket is no longer present
        wait.until(EC.invisibility_of_element((By.XPATH, ticket_number)))

        # DB
        sql = """SELECT [Id]
      ,[AssociatedTicketId]
      ,[ExternalTicketId]
      ,[TicketTypeId]
      ,[OperatorId]
      ,[HaulerId]
      ,[DriverShiftId]
      ,[DriverId]
      ,[VehicleId]
      ,[TrailerId]
      ,[ManifestNumber]
      ,[WorkOrderId]
      ,[LoadTypeId]
      ,[SourceOutletId]
      ,[SourceWellPadId]
      ,[SourceTankId]
      ,[SourceVolume]
      ,[IntendedDestinationOutletId]
      ,[IntendedDestinationWellPadId]
      ,[IntendedDestinationTankId]
      ,[DestinationOutletId]
      ,[DestinationWellPadId]
      ,[DestinationTankId]
      ,[DestinationVolume]
      ,[Rerouted]
      ,[TicketStatusId]
      ,[TotalAmount]
      ,[InvoiceId]
      ,[Enabled]
        FROM [dbo].[Ticket]
        Where ID = 786462"""

        # What to Verify?
        db_ticket = DBHelper.query_runner_as_dict(db, query=sql)

        # Assert Ticket Status is 11 (Cost Awaiting Review)
        ticket_status_id = db_ticket['results'][0]['TicketStatusId']
        assert int(ticket_status_id) == 11

        driver.quit()




















