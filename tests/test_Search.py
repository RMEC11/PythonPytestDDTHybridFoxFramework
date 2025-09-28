import time
import pytest
from pom.HomePage import HomePage
from pom.SearchPage import SearchPage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):

    def test_search_with_valid_input(self):
        home_page = HomePage(self.driver)
        search_page= home_page.search_product("HP")
        assert search_page.valid_search_result_status()


    def test_search_with_Invalid_input(self):
        home_page = HomePage(self.driver)
        search_page=home_page.search_product("Honda")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.invalid_search_result_status(expected_text)


    def test_search_with_blank_input(self):
        home_page = HomePage(self.driver)
        search_page=home_page.search_product("")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.invalid_search_result_status(expected_text)
