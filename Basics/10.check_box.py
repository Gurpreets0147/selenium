from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker
fake_data = Faker()
# renaming service to "ChromeService"

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://www.thewebtaylor.com/static/tutorials/dummy-checkbox/")  # open URL
time.sleep(4)
print(driver.find_element(By.XPATH, '/html/body/div[4]/ul/li[1]/span').is_selected())
time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div[2]/ul/li/span').click()
time.sleep(4)
print(driver.find_element(By.XPATH, '/html/body/div[2]/ul/li/span').is_selected())
time.sleep(4)