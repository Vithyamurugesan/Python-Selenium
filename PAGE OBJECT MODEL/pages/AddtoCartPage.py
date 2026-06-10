from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartPage:

    add_to_cart_button_xpath = "//button[@id='button-cart']"
    success_message_xpath = "//div[contains(@class,'alert-success')]"

    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart_button(self):
        self.driver.find_element(By.XPATH,self.add_to_cart_button_xpath).click()

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(EC.visibility_of_element_located((By.XPATH, self.success_message_xpath)))
        return success_message.text