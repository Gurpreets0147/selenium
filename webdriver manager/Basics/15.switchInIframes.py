from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
def jss():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
    driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="iframeResult"]')) #parent iframe
    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/iframe'))
    sleep(3)
    driver.find_element(By.XPATH,'//*[@id="navbtn_menu"]').click()
    sleep(3)
jss()