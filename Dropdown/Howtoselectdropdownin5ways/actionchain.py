from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/select-menu")
dropdown = driver.find_element(By.ID, "selectOne")
ActionChains(driver).move_to_element(dropdown).click().send_keys("Dr.").send_keys(Keys.ENTER).perform()
time.sleep(3)
driver.quit()