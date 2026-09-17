import pytest

from api.api_client import ApiClient
from config.settings import ENVIRONMENTS, API_ENVIRONMENTS
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


@pytest.fixture(scope="session")
def api_base_url(request):
    env = request.config.getoption("--env")
    return API_ENVIRONMENTS[env]


@pytest.fixture(scope="session")
def api_client(api_base_url):
    return ApiClient(api_base_url)


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", choices=["qa", "int", "preprod"]
    )
