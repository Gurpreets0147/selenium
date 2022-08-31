from calendar import LocaleTextCalendar
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep


def jss():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://demo.guru99.com/test/drag_drop.html")
    sleep(3)
    source=driver.find_element(By.XPATH,"//li[@id='credit']//a[@class='button button-orange']")
    destination=driver.find_element(By.XPATH, "//ol[@id='bank']//li[@class='placeholder']")
    sleep(2)
    # ActionChains(driver).drag_and_drop(source,destination).perform()
    ActionChains(driver).drag_and_drop_by_offset(source,162,242).perform() # X and y cordinater from source
    sleep(3)

jss()