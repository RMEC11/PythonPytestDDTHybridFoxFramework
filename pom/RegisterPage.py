from selenium.webdriver.common.by import By


class RegisterPage:
    fname = (By.NAME, "firstname")
    lname = (By.ID, "input-lastname")
    reg_email = (By.XPATH, "//input[@type='email']")
    reg_telephone = (By.NAME, "telephone")
    reg_pass = (By.ID, "input-password")
    reg_cnf_pass = (By.NAME, "confirm")
    reg_check_box = (By.XPATH, "//input[@type='checkbox']")
    reg_continue = (By.CSS_SELECTOR, "input[value='Continue']")
    acc_create_confirmation_msg = (By.XPATH, "//div[@id='common-success']/div/div[1]/h1")
    Warning_error = (By.XPATH, "//div[@id='account-register']/div[1]")
    fname_validation_XPATH = '//input[@id="input-firstname"]/following-sibling::div'
    email_validation_Xpath = '//input[@id="input-email"]/following-sibling::div'

    def __init__(self, driver):
        self.driver = driver

    def fname_input(self, fname):
        self.driver.find_element(*self.fname).send_keys(fname)

    def lname_input(self, lname):
        self.driver.find_element(*self.lname).send_keys(lname)

    def email_input(self, email):
        self.driver.find_element(*self.reg_email).send_keys(email)

    def telephone_input(self, telphone):
        self.driver.find_element(*self.reg_telephone).send_keys(telphone)

    def password_input(self, password):
        self.driver.find_element(*self.reg_pass).send_keys(password)

    def cnf_password_input(self, cnfpass):
        self.driver.find_element(*self.reg_cnf_pass).send_keys(cnfpass)

    def check_box_tick(self):
        self.driver.find_element(*self.reg_check_box).click()

    def click_on_continue(self):
        self.driver.find_element(*self.reg_continue).click()

    def account_creation_confirmation_msg(self, expected_msg):
        return self.driver.find_element(*self.acc_create_confirmation_msg).text.__contains__(expected_msg)

    def blank_fileds_warning_error(self, exp_warning):
        return self.driver.find_element(*self.Warning_error).text.__eq__(exp_warning)

    def duplicate_email_fileds_warning_error(self, email_warning):
        return self.driver.find_element(*self.Warning_error).text.__eq__(email_warning)

    def register_process(self,fname,lname,email,telephone,password,cnf_pass,exp_text):
        self.fname_input(fname)
        self.lname_input(lname)
        self.email_input(email)
        self.telephone_input(telephone)
        self.password_input(password)
        self.cnf_password_input(cnf_pass)
        self.check_box_tick()
        self.click_on_continue()
        self.account_creation_confirmation_msg(exp_text)


    def register_process_blank_duplicate(self,fname,lname,email,telephone,password,cnf_pass,exp_text):
        self.fname_input(fname)
        self.lname_input(lname)
        self.email_input(email)
        self.telephone_input(telephone)
        self.password_input(password)
        self.cnf_password_input(cnf_pass)
        self.check_box_tick()
        self.click_on_continue()
        self.blank_fileds_warning_error(exp_text)

    def register_process_email_input_at_last(self,fname,lname,email,telephone,password,cnf_pass,exp_text):
        self.fname_input(fname)
        self.lname_input(lname)
        self.telephone_input(telephone)
        self.password_input(password)
        self.cnf_password_input(cnf_pass)
        self.check_box_tick()
        self.click_on_continue()
        self.email_input(email)
        self.click_on_continue()
        self.account_creation_confirmation_msg(exp_text)

