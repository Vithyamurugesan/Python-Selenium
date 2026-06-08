#scrolldown
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
button = driver.find_element(By.ID, "alert1")
driver.execute_script("window.scrollBy(0,500);")
driver.quit()