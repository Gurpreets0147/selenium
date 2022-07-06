"""
from selenium import webdriver  
driver = webdriver.Chrome(
    executable_path="D:\\Automation\\selenium\\chromedriver.exe")   #path to the webdriver file
driver.get("https://google.com")    #open URL
driver.maximize_window()    #maximize window to full screen
print(driver.title)   #print title of webpage
# driver.close()    #close webbrowser
"""
from selenium import webdriver
# renaming service to "ChromeService"
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://google.com")  # open URL
driver.maximize_window()  # maximize window to full screen
print(driver.title)  # print title of webpage

# driver.close()    #close webbrowser
