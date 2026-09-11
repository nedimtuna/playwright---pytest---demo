import pytest

from playwright.sync_api import expect

@pytest.mark.smoke
def test_inventory_items_visible(authenticated_inventory_page):
    assert (
        authenticated_inventory_page.get_inventory_count() == 6
    ), "Expected exactly 6 inventory items."

@pytest.mark.smoke
def test_add_item_to_cart(authenticated_inventory_page):
    authenticated_inventory_page.add_backpack_to_cart()

    expect(authenticated_inventory_page.page_title).to_have_text("Products")