from data.test_data import STANDARD_USER, VALID_PASSWORD, INVALID_PASSWORD, WRONG_USER

INVALID_LOGIN_SCENARIOS = [
    ("invalid_password", STANDARD_USER, INVALID_PASSWORD),
    ("invalid_username", WRONG_USER, VALID_PASSWORD),
    ("invalid_username_and_password", WRONG_USER, INVALID_PASSWORD),
]
