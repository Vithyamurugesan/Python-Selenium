from selenium.webdriver.common.by import By
from configuration.readProperties import ReadConfig
class LoginPage:

    login_page_url = "https://tutorialsninja.com/demo/index.php?route=account/login"
    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"

    def __init__(self, driver):
        self.driver = driver
    def open_login_page(self):
        self.driver.get(ReadConfig.get_application_url())
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()