from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
def jss():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://login.salesforce.com/?locale=in")
    driver.maximize_window()
    driver.implicitly_wait(10)          #Dynamic wait (Globaly)
    driver.find_element(By.ID,"username").send_keys("Hello_world!")
    driver.find_element(By.ID,"password")
    sleep(2)
jss()