import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

# Open Website
driver.get("https://automationexercise.com/")
time.sleep(3)

print("Home Page Title:", driver.title)


driver.find_element(By.XPATH, "//a[contains(text(),'Signup / Login')]").click()
time.sleep(3)


driver.find_element(By.NAME, "name").send_keys("Vithya")


email = f"vithya{int(time.time())}@gmail.com"
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)


driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
time.sleep(3)

driver.find_element(By.ID, "id_gender2").click()
driver.find_element(By.ID, "password").send_keys("Vithya@20")

Select(driver.find_element(By.ID, "days")).select_by_visible_text("10")
Select(driver.find_element(By.ID, "months")).select_by_visible_text("May")
Select(driver.find_element(By.ID, "years")).select_by_visible_text("2000")


driver.find_element(By.ID, "newsletter").click()
driver.find_element(By.ID, "optin").click()

driver.find_element(By.ID, "first_name").send_keys("Vithya")
driver.find_element(By.ID, "last_name").send_keys("R")
driver.find_element(By.ID, "company").send_keys("ABC Company")
driver.find_element(By.ID, "address1").send_keys("Chennai")
driver.find_element(By.ID, "address2").send_keys("Tamil Nadu")

Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

driver.find_element(By.ID, "state").send_keys("Tamil Nadu")
driver.find_element(By.ID, "city").send_keys("Chennai")
driver.find_element(By.ID, "zipcode").send_keys("600001")
driver.find_element(By.ID, "mobile_number").send_keys("9876543210")

driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()
time.sleep(5)


account_created = driver.find_element(By.XPATH, "//b[text()='Account Created!']")
print("Account Created:", account_created.is_displayed())


driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()
time.sleep(5)


driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
time.sleep(5)


account_deleted = driver.find_element(By.XPATH, "//b[text()='Account Deleted!']")
print("Account Deleted:", account_deleted.is_displayed())


driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()
time.sleep(3)

driver.quit()