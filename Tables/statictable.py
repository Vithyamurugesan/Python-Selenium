from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.leafground.com/table.xhtml")

rows = driver.find_elements(By.XPATH, "//table[@role='grid']/tbody/tr")

for row in rows:
    print(row.text)

driver.quit()