from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://google.com")

actions = ActionChains(driver)

actions.reset_actions()

driver.quit()