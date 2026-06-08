from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/select-menu")
wait = WebDriverWait(driver, 10)

dropdown = wait.until(EC.element_to_be_clickable((By.ID, "withOptGroup")))
dropdown.click()
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Group 1, option 1']")))
option.click()
print("Option selected successfully")