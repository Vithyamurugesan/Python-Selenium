from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/key_presses")
driver.maximize_window()
body = driver.find_element(By.TAG_NAME, "body")
ActionChains(driver).key_down(Keys.SHIFT).send_keys("vithya").key_up(Keys.SHIFT).perform()
driver.quit()