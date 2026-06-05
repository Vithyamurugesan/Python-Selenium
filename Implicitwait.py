from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://automationexercise.com')
wait=driver.implicitly_wait(10)

home = driver.find_element(By.XPATH, "//a[contains(text(),'Home')]")
print("Home Enabled:", home.is_enabled())

testcase_link=driver.find_element(By.XPATH,"//a[contains(text(),'Test Cases')]")
testcase_link.click()

testcase_title = driver.find_element(By.XPATH,"//b[contains(text(),'Test Cases')]")
actual_title = testcase_title.text.strip()
print(actual_title)
expected_title = "TEST CASES"
assert actual_title == expected_title
print("Navigate to test cases page successfully")