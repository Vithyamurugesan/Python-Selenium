import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
print("The website launched successfully")
print("Title:", driver.title)
home = driver.find_element(By.XPATH, "//a[contains(text(),'Home')]")
print("Home Enabled:", home.is_enabled())
assert home.is_displayed(), "Home menu is not displayed"
time.sleep(2)
login_link = driver.find_element(By.XPATH, "//a[contains(text(),'Signup / Login')]")
login_link.click()
print("Login link is clicked successfully")
login_page="https://automationexercise.com/login"
assert login_page
signup=driver.find_element(By.XPATH,"//input[@placeholder='Name']")
time.sleep(2)
signup.send_keys("Jessy")
email=driver.find_element(By.XPATH,"//input[@data-qa='signup-email']")
email.send_keys("jessy123@gmail.com")
time.sleep(5)
driver.quit()


