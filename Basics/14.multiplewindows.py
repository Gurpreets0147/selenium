from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
def jss():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://yatra.com/")
    sleep(3)
    parent_handler= driver.current_window_handle
    print(parent_handler)
    driver.find_element(By.XPATH,'//a[@title="Niyo Global"]//img[@class="conta iner large-banner"]').click()
    print(driver.window_handles)
    sleep(3)
    for handler in driver.window_handles:
        if handler != parent_handler:
            driver.switch_to.window(handler)
            print("pass")




jss()