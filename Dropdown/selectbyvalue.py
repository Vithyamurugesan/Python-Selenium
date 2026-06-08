from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown=driver.find_element(By.XPATH,"//select[@id='dropdown']")
obj=Select(dropdown)
obj.select_by_value('1')
print("Option 1 is selcted in the dropdown")
driver.quit()

