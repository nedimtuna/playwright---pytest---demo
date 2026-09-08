import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from data.test_data import (
    LOCKED_USER,
    STANDARD_USER,
    VALID_PASSWORD,
)
from data.login_scenarios import INVALID_LOGIN_SCENARIOS


@pytest.mark.smoke
def test_valid_login(login_page):
    login_page.login(STANDARD_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(login_page.page)

    expect(inventory_page.page_title).to_have_text("Products")


@pytest.mark.regression
@pytest.mark.parametrize(
    "scenario_name,username,password",
    INVALID_LOGIN_SCENARIOS,
    ids=[scenario[0] for scenario in INVALID_LOGIN_SCENARIOS],
)
def test_invalid_login(login_page, scenario_name, username, password):

    login_page.login(username, password)

    expect(login_page.error_message).to_contain_text("Epic sadface")


@pytest.mark.regression
def test_locked_user(login_page):
    login_page.login(LOCKED_USER, VALID_PASSWORD)

    expect(login_page.error_message).to_contain_text("locked out")

# CI smoke test validation