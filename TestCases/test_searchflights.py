from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages.yatra_launch_page import Launchpage
from Pages.Search_flites_page import SearchFlitesResults
@pytest.mark.usefixtures("setup")
class Test_Verify_filters():
    def test_search_flight(self):
        l_page=Launchpage(self.driver,self.wait)
        l_page.departfrom("Goa")
        l_page.departto("New Delhi")
        l_page.selectDate("21/09/2022")
        l_page.searchFlights()
        sleep(10)
        # l_page.page_scroll()

        # sf_page=SearchFlitesResults(self.driver,self.wait)
        # sf_page.filter_flights()
        # stops = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="dotted-borderbtm"]')))
        # print(len(stops))
        # for stop in stops:
        #     print(f"Stop Text {stop.text}")
        #     assert stop.text == "1 Stop"
        #     print("Result Pass")


