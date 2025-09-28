import time
from datetime import datetime
import pytest
from pom.HomePage import HomePage
from pom.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.reach_to_register_page()
        email = self.random_email_generator()
        expected_text = "Your Account Has Been Created!"
        register_page.register_process("RMEC","sept",email,"1234567890","12345","12345",expected_text)
        assert register_page.account_creation_confirmation_msg(expected_text)


    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.reach_to_register_page()
        email = self.random_email_generator()
        expected_text = "Your Account Has Been Created!"
        register_page.register_process("RMEC", "sept", email, "1234567890", "12345", "12345", expected_text)
        assert register_page.account_creation_confirmation_msg(expected_text)


    def test_register_with_all_fields_except_email(self):
        home_page = HomePage(self.driver)
        register_page=home_page.reach_to_register_page()
        email = self.random_email_generator()
        expected_text = "Your Account Has Been Created!"
        register_page.register_process_email_input_at_last("RMEC", "sept",email, "1234567890", "12345", "12345", expected_text)
        assert register_page.account_creation_confirmation_msg(expected_text)


    def test_register_with_blank_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.reach_to_register_page()
        email = self.random_email_generator()
        expected_text = "Warning: You must agree to the Privacy Policy!"
        register_page.register_process_blank_duplicate("", "","", "", "", "", expected_text)
        register_page.blank_fileds_warning_error(expected_text)

    def test_register_with_duplicate_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.reach_to_register_page()
        expected_text = "Warning: E-Mail Address is already registered!"
        register_page.register_process_blank_duplicate("RMEC", "Sept", "amotooriapril2023@gmail.com", "1234567890", "12345", "12345", expected_text)
        time.sleep(2)
        assert register_page.duplicate_email_fileds_warning_error(expected_text)




