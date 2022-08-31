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
    driver.get("https://www.flipkart.com/computers/computer-components/monitors/pr?sid=6bo%2Cg0i%2C9no&fm[]=neo%2Fmerchandising&fm[]=neo%2Fmerchandising&iid[]=M_ce1a6f68-d7d2-4ae1-875c-0d0877d9a11f_2_372UD5BXDFYS_MC.ECL5SFI77NSY&iid[]=M_e9e89768-144c-4cc0-8cf2-9d3badd297d0_3.W52Y6O5JCN9E&otracker1[]=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&otracker1[]=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_1_NA_view-all_3&cid[]=ECL5SFI77NSY&cid[]=W52Y6O5JCN9E&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.brand%255B%255D%3DSAMSUNG&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTk5OTkiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJNb25pdG9ycyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PTkdBUVRRS0NFWkdWU0MiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19&ppt=None&ppn=None&ssid=i4n37juw3k0000001661423783184&otracker=hp_omu_Best%2Bof%2BElectronics_1_3.dealCard.OMU_W52Y6O5JCN9E_3")
    action = ActionChains(driver)
    sleep(5)
    left_slider=driver.find_element(By.XPATH,"//div[@class='_31Kbhn _28DFQy']//div[@class='_3FdLqY']")
    right_slider=driver.find_element(By.XPATH,"//div[@class='_31Kbhn WC_zGJ']")
    # action.drag_and_drop_by_offset(left_slider,60,0).perform()
    # action.click_and_hold(left_slider).pause(1).move_by_offset(60,0).release().perform()
    action.move_to_element(left_slider).pause(1).click_and_hold(left_slider).pause(1).move_by_offset(60,0).release().perform()
    sleep(2)
    action.drag_and_drop_by_offset(right_slider,-60,0).perform()
    # action.click_and_hold(right_slider).pause(1).move_by_offset(60,0).release().perform()
    # action.move_to_element(right_slider).pause(1).click_and_hold(left_slider).pause(1).move_by_offset(60,0).release().perform()
    sleep(3)

jss()