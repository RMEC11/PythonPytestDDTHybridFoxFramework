import time
import pytest
from selenium.webdriver.common.by import By
from pom.HomePage import HomePage
from pom.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ReadConfiguration



class TestLogin(BaseTest):
    def test_login_with_valid_email_and_password(self):
        user_password =ReadConfiguration.read_configuration("basic info","password")
        home_page = HomePage(self.driver)
        login_page=home_page.reach_to_login_page()
        time.sleep(1)
        expected_link = "Edit your account information"
        login_page.user_login_process(user_password,expected_link)
        assert login_page.account_login_confirmation_edit_profile_link(expected_link)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page=home_page.reach_to_login_page()
        time.sleep(1)
        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        login_page.user_login_process_invalid("123456",expected_warning_msg)
        time.sleep(1)
        assert login_page.invalid_cred_warning_message(expected_warning_msg)


    def test_login_with_Invalid_email_and_Valid_password(self):
        home_page = HomePage(self.driver)
        login_page=home_page.reach_to_login_page()
        time.sleep(1)
        expected_warning_msg = "Warning: No match for +++E-Mail Address and/or Password."
        login_page.user_login_process_blank("amotriapril2023@gmail.com","12345",expected_warning_msg)
        assert login_page.invalid_cred_warning_message(expected_warning_msg)


    def test_login_with_blank_email_and_blank_password(self):
        home_page = HomePage(self.driver)
        login_page=home_page.reach_to_login_page()
        time.sleep(1)
        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        login_page.user_login_process_blank("","",expected_warning_msg)
        assert login_page.invalid_cred_warning_message(expected_warning_msg)
