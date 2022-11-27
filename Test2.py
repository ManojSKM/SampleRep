from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "//button[text()='Click Me']").click()
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.accept()
driver.quit()
