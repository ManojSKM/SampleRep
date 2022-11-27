from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.amazon.com/")
print(driver.title)
print(driver.current_url)
driver.execute_script("window.scrollBy(0, document.body.height)")
#value = driver.execute_script("return window.pageYOffset;")
driver.find_element(By.XPATH, "//a[contains(@href, 'Aveeno')]").click()