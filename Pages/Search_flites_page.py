
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver


class SearchFlitesResults(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def filter_flights(self):
        self.driver.find_element(
            By.XPATH, '//p[normalize-space()="1"]').click()
        sleep(4)

