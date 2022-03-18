import unittest

import allure
import pytest

from POM.BaseTest.selenium_driver import SeleniumDriver
from POM.Portal.upass_holder_app import HolderPortal
from utils.read_data import ReadData
from time import sleep
import logging

LOGGER = logging.getLogger(__name__)

"""
    @author             : Somasekhar
    Description         : This method is used to Link record for COVID-19 Test - Antibody(Issuer type: CDC)
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestLinkRecordHealthCovid19Antibody(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    @pytest.mark.run(order=36)
    def test_link_record_health_covid_19_antibody(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)

        with allure.step("Logging to u-pass home page"):
            self.upass_holder_portal.upass_portal_page()
            LOGGER.info("Entered in login page")

        with allure.step("Clicking on Login to existing account button"):
            self.upass_holder_portal.click_existing_account()

        with allure.step("Entering Username"):
            self.upass_holder_portal.enter_username(excel_data)

        with allure.step("Entering Password"):
            self.upass_holder_portal.enter_login_password(test_data["Login"]["Password"])

        with allure.step("Clicking Continue button to Signin"):
            self.upass_holder_portal.click_continue_signin()

        with allure.step("Clicking the records"):
            self.upass_holder_portal.click_records()
            LOGGER.info("Click the records button")

        with allure.step("Clicking the add/get record"):
            self.upass_holder_portal.click_add_or_get_record()
            LOGGER.info("Click add/get record button")

        with allure.step("Clicking the link record"):
            self.upass_holder_portal.click_to_link_record()
            LOGGER.info("Click the link record")

        with allure.step("Selecting holder name"):
            self.upass_holder_portal.select_holder_name()
            LOGGER.info("Select holder name")

        with allure.step("Selecting record category type"):
            self.upass_holder_portal.select_record_category_health()
            LOGGER.info("Select record category")

        with allure.step("Selecting record type: covid 19 antibody"):
            self.upass_holder_portal.select_record_type_covid_19_test_antibody()
            LOGGER.info("Select record type: covid 19 antibody")

        with allure.step("Selecting issuer type: CDC"):
            self.upass_holder_portal.select_issuer_type_cdc()
            LOGGER.info("Select issuer type: CDC")

        with allure.step("Clicking the search records"):
            self.upass_holder_portal.click_search_records()
            LOGGER.info("Click the search records")

        with allure.step("Clicking the save button"):
            self.upass_holder_portal.click_save_record()
            LOGGER.info("Click the save button")

        with allure.step("Clicking Health tab under Records page"):
            self.upass_holder_portal.click_health_tb()
            LOGGER.info("Click Health tab under Records page")

        with allure.step("Verifying covid 19 test antibody health record"):
            self.upass_holder_portal.verify_covid_19_test_antibody()
            LOGGER.info("Verify covid 19 test antibody health record")
