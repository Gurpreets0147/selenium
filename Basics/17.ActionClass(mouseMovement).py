from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

def jss():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    sleep(3)
    action=ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH,"//span[@class='more-arr']"))
    sleep(3)
    action.click(driver.find_element(By.XPATH,"//span[text()='Freight']")).perform()
    sleep(3)
jss()