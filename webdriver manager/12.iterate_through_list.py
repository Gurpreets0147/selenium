
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from faker import Faker
fake_data = Faker()
# renaming service to "ChromeService"

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://google.com/")  # open URL
time.sleep(4)
driver.find_element(By.NAME, 'q').send_keys("google")
time.sleep(2)
serach_results = driver.find_elements(
    By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/ul/li")  # add "li" mannyally
for items in serach_results:
    print(items.text, end=" ")
    if "google pay" in items.text:
        items.click()
        time.sleep(5)
        break
