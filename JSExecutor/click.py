from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
button = driver.find_element(By.ID, "alert1")

driver.execute_script("arguments[0].click();",button)
driver.quit()
