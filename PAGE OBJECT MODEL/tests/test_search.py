import pytest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    @pytest.mark.order(2)
    def test_search_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.enter_product_into_search_box("HP")
        home_page.click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_valid_product()