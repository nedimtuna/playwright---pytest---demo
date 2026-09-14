import pytest

from playwright.sync_api import expect

@pytest.mark.smoke
def test_inventory_items_visible(authenticated_inventory_page):
    expect(authenticated_inventory_page.inventory_items).to_have_count(6)

@pytest.mark.smoke
def test_add_item_to_cart(authenticated_inventory_page):
    authenticated_inventory_page.add_backpack_to_cart()

    expect(authenticated_inventory_page.shopping_cart_badge).to_have_text("1")