import pytest

from data.test_data import STANDARD_USER, VALID_PASSWORD
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.regression
def test_item_visible_in_cart(login_page):
    login_page.login(STANDARD_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(login_page.page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(login_page.page)

    assert cart_page.get_cart_items_count() == 1
