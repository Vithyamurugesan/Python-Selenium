from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.leafground.com/select.xhtml")
driver.maximize_window()

dropdown = driver.find_element(By.XPATH, "(//select)[1]")

driver.execute_script("arguments[0].selectedIndex=2;",dropdown)

driver.execute_script("arguments[0].dispatchEvent(new Event('change'));",dropdown)

input("Press Enter...")
driver.quit()