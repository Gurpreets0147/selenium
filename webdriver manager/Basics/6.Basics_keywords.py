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
driver.find_element(By.NAME, "q").send_keys("google")
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
time.sleep(4)
print(driver.current_url)
time.sleep(4)
print(driver.title)
time.sleep(4)
driver.maximize_window()
time.sleep(4)
driver.fullscreen_window()
time.sleep(4)
driver.refresh()
time.sleep(4)
driver.maximize_window()
time.sleep(4)
driver.back()
time.sleep(4)
driver.forward()
time.sleep(4)
driver.quit()