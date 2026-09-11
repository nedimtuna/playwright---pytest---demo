import pytest

from pages.login_page import LoginPage
from config.settings import ENVIRONMENTS
from data.test_data import STANDARD_USER, VALID_PASSWORD
from pages.inventory_page import InventoryPage


@pytest.fixture(scope="session")
def environment_url(request):
    env = request.config.getoption("--env")
    return ENVIRONMENTS[env]


@pytest.fixture
def login_page(page, environment_url):
    login_page = LoginPage(page, environment_url)
    login_page.open()
    return login_page


@pytest.fixture
def authenticated_inventory_page(login_page):
    login_page.login(STANDARD_USER, VALID_PASSWORD)
    return InventoryPage(login_page.page)


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", choices=["qa", "int", "preprod"]
    )
