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
from set_up.mobile_set_up import MobileSetUp
from helpers.db_helpers import DBHelper
from tests.base import Base
from selenium.webdriver.common.keys import Keys

class TestMobile:

    @pytest.mark.create_simple_ticket
    def test_create_simple_ticket(self,driver,username,password,db):
        ticket_number = MobileSetUp.simple_ticket(self,driver,username,password)

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

        db_ticket = DBHelper.query_runner_as_dict(db, query=sql)
        print(db_ticket)
        db_ticket_number = db_ticket['results'][0]['TicketId']

        assert int(ticket_number) == int(db_ticket_number)


    def test_milk_run(self,driver,username,password,db):
        MobileSetUp.mobile_login(self,driver,username,password)


