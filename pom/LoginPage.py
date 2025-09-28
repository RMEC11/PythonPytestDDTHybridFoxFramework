from selenium.webdriver.common.by import By

from utilities import ReadConfiguration


class LoginPage:
    user_email = (By.NAME, "email")
    user_pass = (By.ID, "input-password")
    login_button = (By.XPATH, "//div[@class='form-group']/following-sibling::input")
    edit_profile_link = (By.LINK_TEXT, "Edit your account information")
    cred_invalid_error = (By.XPATH, "//div[@id='account-login']/div[1]")

    def __init__(self, driver):
        self.driver = driver

    def login_email_input(self):
        user_mailID = ReadConfiguration.read_configuration("basic info", "email")
        self.driver.find_element(*self.user_email).send_keys(user_mailID)

    def login_blank_email_input(self, email):
        self.driver.find_element(*self.user_email).send_keys(email)

    def login_password_input(self, password):
        self.driver.find_element(*self.user_pass).send_keys(password)

    def login_button_submit(self):
        self.driver.find_element(*self.login_button).submit()

    def account_login_confirmation_edit_profile_link(self, expected_link_text):
        return self.driver.find_element(*self.edit_profile_link).text.__eq__(expected_link_text)

    def invalid_cred_warning_message(self, expected_msg):
        return self.driver.find_element(*self.cred_invalid_error).text.__contains__(expected_msg)

    def login_invalid_email_input(self, email):
        self.driver.find_element(*self.user_email).send_keys(email)

    def user_login_process(self, password, expected_text):
        self.login_email_input()
        self.login_password_input(password)
        self.login_button_submit()
        self.account_login_confirmation_edit_profile_link(expected_text)

    def user_login_process_blank(self, email, password, expected_text):
        self.login_blank_email_input(email)
        self.login_password_input(password)
        self.login_button_submit()
        self.invalid_cred_warning_message(expected_text)

    def user_login_process_invalid(self,password, expected_text):
        self.login_email_input()
        self.login_password_input(password)
        self.login_button_submit()
        self.invalid_cred_warning_message(expected_text)
