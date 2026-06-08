from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://automationexercise.com")

subscription = driver.find_element(By.ID, "susbscribe_email")

ActionChains(driver).scroll_to_element(subscription).perform()

driver.quit()