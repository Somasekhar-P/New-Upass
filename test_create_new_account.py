import unittest

import allure
import pytest

from POM.BaseTest.selenium_driver import SeleniumDriver
from POM.Portal.upass_holder_app import HolderPortal
import logging
from utils.read_data import ReadData

LOGGER = logging.getLogger(__name__)

"""
@author        : Srinivas Reddy
Description    : This class is used to create New User account 
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestCreateAccount(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    LOGGER.info('Creating New User account')

    @pytest.mark.run(order=1)
    def test_create_account(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()

        with allure.step("Logging to u-pass home page"):
            self.upass_holder_portal.upass_portal_page()

        with allure.step("Clicking create new login button"):
            self.upass_holder_portal.click_create_new_login_btn()

        with allure.step("Entering Full name"):
            self.upass_holder_portal.enter_full_legal_name()

        with allure.step("Entering Email"):
            self.upass_holder_portal.enter_Email()

        with allure.step("Entering date of birth"):
            self.upass_holder_portal.enter_birthdate(test_data["details"]["dob"])

        with allure.step("Entering Phone Number"):
            self.upass_holder_portal.enter_phone_number(test_data["details"]["phone"])

        with allure.step("Entering Insurance Provider Name"):
            self.upass_holder_portal.enter_insurance_provider(test_data["details"]["insurance provider"])

        with allure.step("Entering Member Id"):
            self.upass_holder_portal.enter_member_id(test_data["details"]["member id"])

        with allure.step("Entering Group Member"):
            self.upass_holder_portal.enter_group_number(test_data["details"]["group id"])

        with allure.step("Selecting Sex"):
            self.upass_holder_portal.select_sex_male()

        with allure.step("Selecting Race"):
            self.upass_holder_portal.select_race_white()

        with allure.step("Selecting Race"):
            self.upass_holder_portal.select_ethnicity_h()

        with allure.step("Entering Password"):
            self.upass_holder_portal.enter_password(test_data["details"]["password"])

        with allure.step("Entering confirm password"):
            self.upass_holder_portal.enter_Confirm_password(test_data["details"]["password"])

        with allure.step("Enabling Push Notification"):
            self.upass_holder_portal.enable_push_notifications()

        with allure.step("Enabling SMS Notification"):
            self.upass_holder_portal.enable_sms_notifications()

        with allure.step("Clicking I Agree Button"):
            self.upass_holder_portal.click_i_agree()

        with allure.step("Clicking Continue button"):
            self.upass_holder_portal.click_continue()

        with allure.step("Clicking Continue button"):
            self.upass_holder_portal.click_continue_button()

        with allure.step("Clicking Go To U-Pass button"):
            self.upass_holder_portal.click_go_to_upass()

        with allure.step("Verifying New Account"):
            self.upass_holder_portal.verify_new_account()
