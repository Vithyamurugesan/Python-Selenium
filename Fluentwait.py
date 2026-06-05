from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://automationexercise.com')

Fluent_wait = WebDriverWait(driver,timeout=15,poll_frequency=0.5)

home = driver.find_element(By.XPATH, "//a[contains(text(),'Home')]")
print("Home Enabled:", home.is_enabled())
wait=WebDriverWait(driver,15)
testcase_link=Fluent_wait.until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Test Cases')]")))
testcase_link.click()

testcase_title=Fluent_wait.until(EC.visibility_of_element_located((By.XPATH,"//b[contains(text(),'Test Cases')]")))
actual_title = testcase_title.text.strip()
print(actual_title)
expected_title = "TEST CASES"
assert actual_title == expected_title
print("Navigate to test cases page successfully")
