from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

def jss():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
    sleep(3)
    driver.switch_to.frame('iframeResult') 
    sleep(3)
    driver.find_element(By.XPATH,'//button[text()="Try it"]').click()
    sleep(3)
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.send_keys("hello World")
    sleep(1)
    driver.switch_to.alert.accept()
    # driver.switch_to.alert.dismiss()
    sleep(3)
jss()