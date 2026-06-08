from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

doubleclick_button=driver.find_element(By.XPATH,"//button[@ondblclick='dblclickAlert()']")
action=ActionChains(driver)
action.double_click(doubleclick_button).perform()
print("Double click performed")
driver.quit()

