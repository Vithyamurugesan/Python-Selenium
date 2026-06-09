import pytest
from selenium.webdriver.common.by import By 
import read_config
import time
@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_validlogin(self):
        self.driver.find_element(By.ID,value="login2").click()
        uname=read_config.get_config("login","username")
        passd=read_config.get_config("login","password")
        self.driver.find_element(By.ID,value='loginusername').send_keys(uname)
        self.driver.find_element(By.ID,value='loginpassword').send_keys(passd)
        self.driver.find_element(By.XPATH,value="//button[text()='Log in']").click()
        time.sleep(5)
        assert self.driver.find_element(By.ID,value='logout2').is_displayed()

    def test_invalidlogin(self):
        self.driver.find_element(By.ID,value="login2").click()
        uname=read_config.get_config("invalid","invalidusername")
        passd=read_config.get_config("invalid","invalidpassword")
        self.driver.find_element(By.ID,value='loginusername').send_keys(uname)
        self.driver.find_element(By.ID,value='loginpassword').send_keys(passd)
        self.driver.find_element(By.XPATH,value="//button[text()='Log in']").click()
        time.sleep(5)
        alert = self.driver.switch_to.alert
        assert alert.text == "Wrong password."
        alert.accept()
