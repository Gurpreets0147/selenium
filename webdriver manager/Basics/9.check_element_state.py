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

driver.get("https://training.openspan.com/login")  # open URL
time.sleep(4)
print(driver.find_element(By.XPATH, '//*[@id="login_button"]').is_enabled())
driver.find_element(
    By.XPATH, '//*[@id="user_name"]').send_keys(fake_data.name())
driver.find_element(
    By.XPATH, '//*[@id="user_pass"]').send_keys(fake_data.password())
time.sleep(4)
print(driver.find_element(By.XPATH, '//*[@id="login_button"]').is_enabled())
time.sleep(4)
