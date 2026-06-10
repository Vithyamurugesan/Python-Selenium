import pytest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from pages.AddtoCartPage import AddToCartPage

@pytest.mark.usefixtures("setup")
class TestAddToCart:

    @pytest.mark.order(3)
    def test_add_product_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.enter_product_into_search_box("HP")
        home_page.click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_valid_product()
        search_page.click_valid_product()
        cart_page = AddToCartPage(self.driver)
        cart_page.click_add_to_cart_button()
        assert "Success: You have added HP LP3065 to your shopping cart!" in cart_page.get_success_message()