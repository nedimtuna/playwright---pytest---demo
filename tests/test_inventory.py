import pytest

from data.test_data import STANDARD_USER, VALID_PASSWORD
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

@pytest.mark.smoke
def test_inventory_items_visible(login_page):
    login_page.login(STANDARD_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(login_page.page)

    assert (
        inventory_page.get_inventory_count() == 6
    ), "Expected exactly 6 inventory items."

@pytest.mark.smoke
def test_add_item_to_cart(login_page):
    login_page.login(STANDARD_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(login_page.page)

    inventory_page.add_backpack_to_cart()

    expect(inventory_page.page_title).to_have_text("Products")