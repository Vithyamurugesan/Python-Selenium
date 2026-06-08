from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://www.leafground.com/select.xhtml")
driver.maximize_window()
dropdown = driver.find_element(By.CLASS_NAME, "ui-selectonemenu")
select = Select(dropdown)
select=Select(dropdown)
options=select.options
for option in options:
    print(option.text)


