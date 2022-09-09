from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Launchpage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def departfrom(self, location):
        self.driver.find_element(
            By.XPATH, "//a[@id='booking_engine_flights']").click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@id='BE_flight_origin_city']"))).click()
        # driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").click()
        listitms = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//p[@class="ac_cityname"]'))).find_elements(By.XPATH, '//p[@class="ac_cityname"]')
        # listitms=driver.find_elements(By.XPATH,'//p[@class="ac_cityname"]')
        for itm in listitms:
            # print(itm.text)
            if location in itm.text:
                itm.click()
                break

    def departto(self, location):
        listitms = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//p[@class="ac_cityname"]'))).find_elements(By.XPATH, '//p[@class="ac_cityname"]')
        print("length", len(listitms))
        for itm in listitms:
            # print(itm.text)
            if location in itm.text:
                itm.click()
                break

    def selectDate(self, date):
        # //td[@id='21/09/2022']
        self.driver.find_element(
            By.XPATH, "//input[@id='BE_flight_origin_date']").click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//td[@id='{date}']"))).find_element(By.XPATH, f"//td[@id='{date}']").click()

    def searchFlights(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//input[@value="Search Flights"]'))).find_element(By.XPATH, '//input[@value="Search Flights"]').click()
