from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")

element = driver.find_element(By.ID, "drop1")
driver.execute_script("arguments[0].scrollIntoView();",element)
print("Scroll to element using the scrollintoview")
driver.quit()
