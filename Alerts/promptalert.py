from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, "prompt").click()

alert = driver.switch_to.alert

print("Alert Text:", alert.text)

alert.send_keys("Vithya")

alert.accept()

time.sleep(3)
driver.quit()