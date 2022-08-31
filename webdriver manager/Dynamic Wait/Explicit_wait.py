from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.yatra.com/")
driver.maximize_window()

def Demo():
    wait =WebDriverWait(driver, 10)
    driver.find_element(By.XPATH,"//a[@id='booking_engine_flights']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_city']"))).click()
    # driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").click()
    listitms=wait.until(EC.element_to_be_clickable((By.XPATH,'//p[@class="ac_cityname"]'))).find_elements(By.XPATH,'//p[@class="ac_cityname"]')
    # listitms=driver.find_elements(By.XPATH,'//p[@class="ac_cityname"]')
    print("length",len(listitms))
    for itm in listitms:
        # print(itm.text)
        if "Mumbai" in itm.text:
            itm.click()
            break
    listitm=wait.until(EC.element_to_be_clickable((By.XPATH,'//p[@class="ac_cityname"]'))).find_elements(By.XPATH,'//p[@class="ac_cityname"]')
    print("length",len(listitms))
    for it in listitm:
        # print(itm.text)
        if "Goa" in it.text:
            it.click()
            break


Demo()
sleep(2)


