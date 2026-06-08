from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.leafground.com/drag.xhtml")
driver.maximize_window()
drag=driver.find_element(By.XPATH,"//span[@class='ui-panel-title']")
action=ActionChains(driver)
action.drag_and_drop_by_offset(drag,500,0).perform()
driver.quit()


