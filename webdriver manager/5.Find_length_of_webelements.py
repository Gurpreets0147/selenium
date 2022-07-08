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
time.sleep(10)
d=driver.find_elements(By.TAG_NAME, "a")
print(len(d))
for i in d:
    print(i.text)
time.sleep(5)