import pytest

from data.test_data import (
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE,
    STANDARD_USER,
    VALID_PASSWORD,
)
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect


@pytest.mark.smoke
def test_complete_checkout_flow(login_page):
    login_page.login(STANDARD_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(login_page.page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(login_page.page)

    assert cart_page.get_cart_items_count() == 1

    cart_page.click_checkout()

    checkout_page = CheckoutPage(login_page.page)

    checkout_page.fill_checkout_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    expect(checkout_page.success_message).to_have_text("Thank you for your order!")
