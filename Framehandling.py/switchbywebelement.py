from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/iframes.html")

frame = driver.find_element(By.ID, "iframe1")

driver.switch_to.frame(frame)

print("Inside Frame")

driver.switch_to.default_content()

driver.quit()