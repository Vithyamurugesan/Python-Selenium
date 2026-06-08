from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://www.leafground.com/button.xhtml")
driver.maximize_window()

click_button=driver.find_element(By.XPATH,"//span[text()='Click']")
action=ActionChains(driver)
action.click(click_button).perform()
print("Click action performed using ActionChains method click")
driver.quit()

