from selenium.webdriver.common.by import By


class SearchPage:
    search_result = (By.LINK_TEXT, "HP LP3065")
    invalid_search_result = (By.XPATH,"//p[text()='There is no product that matches the search criteria.']")

    def __init__(self, driver):
        self.driver = driver

    def valid_search_result_status(self):
        return self.driver.find_element(*self.search_result).is_displayed()

    def invalid_search_result_status(self,expected_result):
        return self.driver.find_element(*self.invalid_search_result).text.__eq__(expected_result)

