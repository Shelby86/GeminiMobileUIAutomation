import logging as log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from helpers.login import Login


class TestSimpleTickets:



    # Now optionally here is would be great if we could get the text for the ticket number
    # To verify it is on the completions page
    # We could also get the other info to verify


    @pytest.mark.simple_ticket
    def test_simple_ticket(self,driver,wait):
        Login.login(driver)
        time.sleep(10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.ticket_button_element)))
        time.sleep(5)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Ticket']").click()

        driver.find_element(By.XPATH, self.ticket_button_element).click()
        time.sleep(5)

        # pull volume
        wait.until(EC.visibility_of_element_located((By.XPATH, self.pull_volume_element)))
        pull_volume_button = driver.find_element(By.XPATH, self.pull_volume_element).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, self.ok_button_pop_up_element)))
        driver.find_element(By.XPATH, self.ok_button_pop_up_element).click()
        pull_volume_button.click()
        pull_volume_button.sund_keys(55)

        # Source
        wait.until(EC.visibility_of_element_located((By.XPATH, self.source_field_element)))
        driver.find_element(By.XPATH, self.source_field_element).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, self.adams_1_element)))
        driver.find_element(By.XPATH, self.adams_1_element).click()

        # destination
        wait.until(EC.visibility_of_element_located((By.XPATH, self.intended_destination_drop_off_element)))
        driver.find_element(By.XPATH, self.intended_destination_drop_off_element).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, self.adams_2_element)))
        driver.find_element(By.XPATH, self.adams_2_element).click()

        # drop off
        driver.find_element(By.XPATH, self.complete_drop_off_button_element).click()

        time.sleep(5)






        driver.quit()




