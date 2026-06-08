from selenium import webdriver
from selenium.webdriver.common.by import By 
driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
confirm=driver.find_element(By.ID,'confirm')
confirm.click()
alert=driver.switch_to.alert
print(alert.text)
#alert.accept()
alert.dismiss()
print("Alert is dismissed")

driver.quit()