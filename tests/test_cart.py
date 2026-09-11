import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage


@pytest.mark.regression
def test_item_visible_in_cart(authenticated_inventory_page):
    authenticated_inventory_page.add_backpack_to_cart()
    authenticated_inventory_page.open_cart()

    cart_page = CartPage(authenticated_inventory_page.page)

    expect(cart_page.cart_item).to_have_count(1)