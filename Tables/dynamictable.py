from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.leafground.com/table.xhtml")

rows = driver.find_elements(By.XPATH, "//table//tbody/tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    print([col.text for col in cols])

driver.quit()