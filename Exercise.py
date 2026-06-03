import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.co.in")
print(driver.title)
search=driver.find_element(By.ID,value="APjFqb")
print("Search box enabled:", search.is_enabled())
time.sleep(5)
search.send_keys("selenium")
time.sleep(5)
search_button=driver.find_element(By.NAME,"btnK")
print("Search button enabled:", search_button.is_enabled())
search_button.click()
driver.quit()

