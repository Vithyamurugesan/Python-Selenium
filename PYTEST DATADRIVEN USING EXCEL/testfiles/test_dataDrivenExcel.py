import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from Utilities import excelReader
from Utilities import logCreator


@pytest.mark.parametrize(
    "username,password",
    excelReader.get_data("ExcelFiles/logindata.xlsx", "login")
)
class TestLogindemo:

    log = logCreator.log_creator()

    def test_validlogin(self, username, password):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.demoblaze.com/")

        self.log.info("Application Launched")

        driver.find_element(By.ID, "login2").click()
        time.sleep(2)

        driver.find_element(By.ID, "loginusername").send_keys(username)
        driver.find_element(By.ID, "loginpassword").send_keys(password)

        driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        self.log.info(f"Login attempted with Username={username}")

        time.sleep(5)

        try:
            logout_btn = driver.find_element(By.ID, "logout2")

            if logout_btn.is_displayed():
                self.log.info("Login Successful")
                assert True

        except NoSuchElementException:
            self.log.error("Login Failed")
            pytest.fail(f"Login failed for Username={username}")

        finally:
            driver.quit()