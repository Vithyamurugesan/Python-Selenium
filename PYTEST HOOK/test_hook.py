import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 
import pytest_check as check

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo")
  
def teardown_function(function):
    driver.quit()

def test_valid_product():
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT, "H LP3065").is_displayed()


def test_invalid_product():
    driver.find_element(By.NAME, "search").send_keys("XYZ123")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    message = driver.find_element(
            By.XPATH, "//p[contains(text(),'There is no product')]"
        ).text
    assert "no product" in message.lower()


def test_noproduct():
    driver.find_element(By.NAME, "search").send_keys("")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    assert "Search" in driver.title