from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.leafground.com/drag.xhtml")
driver.maximize_window()
drag=driver.find_element(By.XPATH,"//span[@class='ui-panel-title']")
action=ActionChains(driver)
ActionChains(driver).click_and_hold(drag).move_by_offset(500, 0).release().perform()
driver.quit()

