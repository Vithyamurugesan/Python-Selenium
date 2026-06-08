from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

parent = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Click Here").click()

all_windows = driver.window_handles

for window in all_windows:
    if window != parent:
        driver.switch_to.window(window)
        print("Child Title:", driver.title)
        driver.close()

driver.switch_to.window(parent)
print("Parent Title:", driver.title)

driver.quit()