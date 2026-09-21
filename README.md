# Playwright Pytest Automation Framework

A QA automation portfolio project built with **Python, Playwright, pytest, and Requests**.

The framework demonstrates automated **UI and API testing**, reusable test architecture, cross-browser execution, parallel testing, HTML reporting, and CI/CD integration with GitHub Actions.

## Key Features

- UI automation with Playwright
- API testing with Requests
- Page Object Model (POM)
- Reusable pytest fixtures
- Data-driven and parametrized tests
- Smoke, regression, and API test markers
- Chromium and Firefox cross-browser testing
- Parallel execution with pytest-xdist
- Environment-based configuration
- HTML test reports with pytest-html
- Screenshots and Playwright traces on CI failures
- GitHub Actions CI/CD
- Separate PR and main branch test strategies

## Test Coverage

The framework currently contains **16 unique automated tests**:

- **9 UI tests**
- **7 API tests**

UI coverage includes login, invalid authentication scenarios, inventory validation, cart functionality, and checkout flows.

API coverage includes GET, POST, PUT, PATCH, and DELETE requests, as well as positive and negative response validation.

## CI/CD Strategy

GitHub Actions automatically executes the test suite.

### Pull Requests

Pull requests to `main` run:

- UI smoke tests on Chromium
- UI smoke tests on Firefox
- API tests

This provides fast feedback before changes are merged.

### Main Branch

Pushes to `main` run:

- Full UI suite on Chromium
- Full UI suite on Firefox
- API tests

HTML reports are generated for each test job. Playwright screenshots and traces are retained when UI tests fail.

## Project Structure

```text
playwright-pytest-demo/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── api/
│   ├── __init__.py
│   └── api_client.py
│
├── config/
│   └── settings.py
│
├── data/
│   ├── login_scenarios.py
│   └── test_data.py
│
├── pages/
│   ├── __init__.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── tests/
│   ├── api/
│   │   └── test_users_api.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_inventory.py
│   └── test_login.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### Architecture

- **`pages/`** — Page Object Model classes containing UI locators and page-specific actions.
- **`tests/`** — Automated UI and API test cases.
- **`tests/api/`** — API test suite separated from browser-based UI tests.
- **`api/`** — Reusable API client built on top of `requests.Session`.
- **`data/`** — Test data and parametrized login scenarios.
- **`config/`** — Environment-specific UI and API configuration.
- **`conftest.py`** — Shared pytest fixtures, environment configuration, API client setup, and custom command-line options.
- **`pytest.ini`** — pytest configuration and custom test markers.
- **`.github/workflows/`** — GitHub Actions CI configuration.

## Technologies

- Python 3.12
- Playwright
- pytest
- Requests
- pytest-playwright
- pytest-xdist
- pytest-html
- GitHub Actions

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nedimtuna/playwright---pytest---demo.git
cd playwright---pytest---demo
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

## Running the Tests

### Run the Complete Test Suite

```bash
pytest -v
```

### Run Smoke Tests

```bash
pytest -v -m smoke
```

### Run Regression Tests

```bash
pytest -v -m regression
```

### Run API Tests

```bash
pytest -v -m api
```

### Run UI Tests on Chromium

```bash
pytest -v tests --ignore=tests/api --browser=chromium
```

### Run UI Tests on Firefox

```bash
pytest -v tests --ignore=tests/api --browser=firefox
```

### Run Tests in Parallel

```bash
pytest -v -n 2
```

### Generate an HTML Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

The generated report is available at:

```text
reports/report.html
```

## Environment Configuration

The framework supports multiple test environments through the `--env` command-line option.

Available environments:

- `qa`
- `int`
- `preprod`

The default environment is `qa`.

Example:

```bash
pytest -v --env=qa
```

Environment URLs are managed centrally in:

```text
config/settings.py
```

This keeps environment configuration separate from test logic and allows tests to run against different environments without modifying test code.

## API Authentication

The API client supports optional authentication through the `REQRES_API_KEY` environment variable.

On Windows PowerShell:

```powershell
$env:REQRES_API_KEY="your_api_key"
```

The API client automatically adds the API key to the request headers when the environment variable is available.

The API key is not stored in the repository, keeping sensitive credentials outside the source code.
