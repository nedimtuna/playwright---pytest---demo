import pytest

from pages.cart_page import CartPage


@pytest.mark.regression
def test_item_visible_in_cart(authenticated_inventory_page):
    authenticated_inventory_page.add_backpack_to_cart()
    authenticated_inventory_page.open_cart()

    cart_page = CartPage(authenticated_inventory_page.page)

    assert cart_page.get_cart_items_count() == 1