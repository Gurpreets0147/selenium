from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# renaming service to "ChromeService"

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://google.com/")  # open URL
sleep(4)
i=driver.find_element(By.XPATH, '//div[@class="FPdoLc lJ9FBc"]//input[@class="gNO89b" ][@value="Google Search"]')
driver.get_screenshot_as_file("test.png") # Get screenshot of 
i.screenshot("sc1.png")
sleep(2)
