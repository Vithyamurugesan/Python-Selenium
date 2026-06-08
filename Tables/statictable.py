from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")

rows = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")

for row in rows:
    print(row.text)

driver.quit()