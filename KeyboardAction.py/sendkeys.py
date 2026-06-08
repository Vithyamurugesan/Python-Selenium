from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/key_presses")
driver.maximize_window()
giventext=driver.find_element(By.XPATH,"//form//input[@id='target']")
giventext.send_keys("Vithya")
driver.quit()


