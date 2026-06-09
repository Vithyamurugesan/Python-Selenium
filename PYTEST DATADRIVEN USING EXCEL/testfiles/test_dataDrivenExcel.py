import pytest

from selenium.webdriver.common.by import By 
from selenium import webdriver
import time
from Utilities import excelReader
from Utilities import logCreator

@pytest.mark.parametrize("username,password",excelReader.get_data("ExcelFiles/logindata.xlsx", "login"))

class TestLogindemo:
    log=logCreator.log_generator()
    def test_validlogin(self,username,password):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        self.log.info("Application Launched")
        self.driver.find_element(By.ID,value="login2").click()
        time.sleep(5)
        self.driver.find_element(By.ID,value='loginusername').send_keys(username)
        time.sleep(5)
        self.driver.find_element(By.ID,value='loginpassword').send_keys(password)
        self.driver.find_element(By.XPATH,value="//button[text()='Log in']").click()
        self.log.info("Logineg successfully")
        time.sleep(5) 
        assert self.driver.find_element(By.ID,value='logout2').is_displayed()
        self.log.info("Assertion got success")
        self.driver.quit()


