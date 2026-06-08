from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/drag.xhtml")

dropsource=driver.find_element(By.XPATH,"//div[@id='form:drag_content']")
droptarget=driver.find_element(By.XPATH,"//div[@id='form:drop_content']")

action=ActionChains(driver)
action.drag_and_drop(dropsource,droptarget)
driver.quit()