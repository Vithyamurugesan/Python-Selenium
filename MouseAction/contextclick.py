from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/context_menu")
box = driver.find_element(By.ID, "hot-spot")
ActionChains(driver).context_click(box).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.quit()