from selenium import webdriver
from selenium.webdriver.common.by import By 
driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
simple=driver.find_element(By.ID,'alert1')
simple.click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
driver.quit()