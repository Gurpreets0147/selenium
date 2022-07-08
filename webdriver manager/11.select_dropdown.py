from select import select
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from faker import Faker
fake_data = Faker()
# renaming service to "ChromeService"

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")  # open URL
time.sleep(4)
dropdown=Select(driver.find_element(By.XPATH, '//*[@id="post-2646"]/div[2]/div/div/div/p/select'))
dropdown.select_by_index(1)
time.sleep(4)
dropdown.select_by_value('ASM')
time.sleep(4)
dropdown.select_by_visible_text('Aruba')
time.sleep(4)
