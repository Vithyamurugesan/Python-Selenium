from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.com")

driver.switch_to.new_window('window')

driver.get("https://selenium.dev")

print(driver.title)

driver.quit()