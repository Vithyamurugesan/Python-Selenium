from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/iframes.html")

driver.switch_to.frame(0)

print("Inside Frame")

driver.switch_to.default_content()

driver.quit()