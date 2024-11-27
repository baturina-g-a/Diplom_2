import pytest

import data
import helpers
from methods.user_methods import UserMethods


@pytest.fixture()
def create_and_delete_user():
    payload = {
        "email": helpers.create_random_email(),
        "password": helpers.generate_random_string(8),
        "name": helpers.generate_random_string(8)
    }
    user_methods = UserMethods()
    response = user_methods.post_create_user(payload)
    yield response[1]['accessToken']
    user_methods.delete_user(response[1]['accessToken'])


@pytest.fixture()
def login_user():
    payload = data.EXISTING_USER
    user_methods = UserMethods()
    response = user_methods.post_login_user(payload)
    yield response[1]['accessToken']
