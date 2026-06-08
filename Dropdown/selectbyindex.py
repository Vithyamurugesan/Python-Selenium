from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://www.leafground.com/select.xhtml")
driver.maximize_window()

select_selenium=driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']")
dropdown=Select(select_selenium)
dropdown.select_by_index(2)
print("Puppeeter is selected in dropdown")
