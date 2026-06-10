import pytest

from pages.LoginPage import LoginPage
from pages.AccountPage import AccountPage
from configuration.readProperties import ReadConfig
from utilities.logCreator import log_generator


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    logger = log_generator()

    @pytest.mark.order(1)
    def test_login_with_valid_credentials(self):
        self.logger.info("******** Login Test Started ********")
        login_page = LoginPage(self.driver)
        self.logger.info("Opening Login Page")
        login_page.open_login_page()
        login_page.enter_email(ReadConfig.get_email())
        self.logger.info("Entered Email")
        login_page.enter_password(ReadConfig.get_password())
        self.logger.info("Entered Password")
        login_page.click_login_button()
        self.logger.info("Clicked Login Button")
        account_page = AccountPage(self.driver)
        status = account_page.display_status_of_edit_account_information()
        if status:
            self.logger.info("Login Passed")
            assert True
        else:
            self.logger.error("Login Failed")
            assert False
        self.logger.info("******** Login Test Finished ********")