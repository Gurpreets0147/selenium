from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://google.com")
driver.maximize_window()

def Demo():
    #  To remedy our buggy instruction set from earlier, we could employ a wait to have the findElement call wait until the dynamically added element from the script has been added to the DOM:
    # WebDriverWait(driver, timeout=3).until(some_condition)
    return driver.find_element(By.NAME,"btnK")
   
e=WebDriverWait(driver, timeout=10).until(Demo)
e.click()

sleep(2)
# driver.find_element(By.ID, "username").send_keys("Hello_world!")
# driver.find_element(By.ID, "password")

