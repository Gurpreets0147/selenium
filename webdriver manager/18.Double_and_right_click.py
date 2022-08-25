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
    driver.get("http://demo.guru99.com/test/simple_context_menu.html")
    action = ActionChains(driver)
    sleep(3)
    action.context_click(driver.find_element(
        By.XPATH, '//span[@class="context-menu-one btn btn-neutral"]')).perform()
    sleep(3)
    action.click(driver.find_element(
        By.XPATH, "//span[normalize-space()='Paste']")).perform()
    sleep(3)
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
    sleep(3)

    action.double_click(driver.find_element(
        By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")).perform()
    sleep(3)
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
    sleep(3)


jss()
