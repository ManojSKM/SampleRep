import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("H:\\New Python Related Starting From Beginnig\\SDET Folders\\Selenium Folders\\Browser Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
search_text = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
search_text.send_keys("selenium")
search_icon = driver.find_element(By.XPATH, "//input[@type='submit']")
search_icon.click()
time.sleep(5)
links = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']//a")
for link in links:
    link.click()
windowIDs = driver.window_handles
for win_id in windowIDs:
    driver.switch_to.window(win_id)
    #if driver.title == "Selenium dioxide - Wikipedia":
    print(driver.title)
    print(win_id)
    #driver.close()
driver.quit()






