from selenium.webdriver.common.by import By

from pom.LoginPage import LoginPage
from pom.RegisterPage import RegisterPage
from pom.SearchPage import SearchPage


class HomePage:
    search_box_field = (By.XPATH, "//input[contains(@class,'form-control')]")
    search_button = (By.XPATH, "//i[contains(@class,'fa-search')]")
    My_Account = (By.LINK_TEXT, "My Account")
    Login_link = (By.LINK_TEXT, "Login")
    Register_link = (By.LINK_TEXT, "Register")

    def __init__(self, driver):
        self.driver = driver

    def enter_product_name_in_search_field(self, product_name):
        self.driver.find_element(*self.search_box_field).click()
        self.driver.find_element(*self.search_box_field).clear()
        self.driver.find_element(*self.search_box_field).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(*self.search_button).click()
        return SearchPage(self.driver)

    def click_on_My_Account(self):
        self.driver.find_element(*self.My_Account).click()

    def click_on_Login(self):
        self.driver.find_element(*self.Login_link).click()
        return LoginPage(self.driver)

    def click_on_Register(self):
        self.driver.find_element(*self.Register_link).click()
        return RegisterPage(self.driver)

    def search_product(self, product_name):
        self.enter_product_name_in_search_field(product_name)
        self.click_on_search_button()
        return SearchPage(self.driver)

    def reach_to_login_page(self):
        self.click_on_My_Account()
        self.click_on_Login()
        return LoginPage(self.driver)

    def reach_to_register_page(self):
        self.click_on_My_Account()
        self.click_on_Register()
        return RegisterPage(self.driver)
