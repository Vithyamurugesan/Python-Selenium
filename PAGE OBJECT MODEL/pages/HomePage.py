from selenium.webdriver.common.by import By

class HomePage:

    URL = "https://tutorialsninja.com/demo/"
    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_product_into_search_box(self, product_name):
        self.driver.find_element(By.NAME,self.search_box_field_name).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()