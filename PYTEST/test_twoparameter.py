import pytest
import time
from selenium import webdriver

@pytest.mark.parametrize('input_browser', ['chrome', 'firefox'])
@pytest.mark.parametrize('input_url', ['https://www.flipkart.com','https://www.amazon.com'])
def test_url_on_browser(input_browser, input_url):

    if input_browser == 'chrome':
        web_driver = webdriver.Chrome()

    elif input_browser == 'firefox':
        web_driver = webdriver.Firefox()

    web_driver.maximize_window()
    web_driver.get(input_url)

    print(web_driver.title)

    time.sleep(2)
    web_driver.quit()