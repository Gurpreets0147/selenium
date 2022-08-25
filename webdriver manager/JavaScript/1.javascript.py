from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
def jss():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.execute_script("window.open('https://google.com', '_self');")
    sleep(3)
    driver.execute_script('document.getElementsByTagName("input")[0].value="helloWorld";')
    sleep(5)
    driver.execute_script("return document.getElementsByTagName('input')[3].click();")
    sleep(5)
jss()