from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# renaming service to "ChromeService"
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://google.com")  # open URL
time.sleep(4)
text=driver.find_element(By.XPATH, '//*[@id="SIvCob"]/a[2]').text
print(text)
time.sleep(4)