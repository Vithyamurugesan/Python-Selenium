import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('input_browser',['chrome','firefox'])
@pytest.mark.parametrize('input_url',['https://www.flipcart.com','https://www.amazon.com'])

def test_url_on_browser(input_browser,input_url):
    if input_browser=='chrome':
        web_driver=webdriver.Chrome()
    if input_browser=='firefox':
        web_driver=webdriver.Firefox()
    web_driver.maximize_window()
    web_driver.get(input_url)
    print(web_driver.title)
    web_driver.quit()