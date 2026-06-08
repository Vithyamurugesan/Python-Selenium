from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = webdriver.Chrome()
driver.get("https://automationexercise.com")

origin = ScrollOrigin.from_viewport(0, 0)

ActionChains(driver)\
    .scroll_from_origin(origin, 0, 1000)\
    .perform()

driver.quit()