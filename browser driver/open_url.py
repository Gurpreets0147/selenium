from selenium import webdriver
driver = webdriver.Chrome(
    executable_path="D:\\Automation\\selenium\\chromedriver.exe")
driver.get("https://google.com")
print(driver.title)
# driver.close()