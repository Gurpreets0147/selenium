import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages.yatra_launch_page import Launchpage

@pytest.mark.usefixtures("setup")
class Test_Verify_filters():
    def test_search_flight(self):
        l_page=Launchpage(self.driver,self.wait)
        l_page.departfrom("Goa")
        l_page.departto("New Delhi")
        l_page.selectDate("21/09/2022")
        l_page.searchFlights()


