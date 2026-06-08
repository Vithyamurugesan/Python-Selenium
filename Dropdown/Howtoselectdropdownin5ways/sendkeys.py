from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/select-menu")


driver.find_element(By.ID, "selectOne").click()

textbox = driver.switch_to.active_element

textbox.send_keys("Dr.")
textbox.send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()