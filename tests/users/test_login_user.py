import pytest

import data
import helpers
from methods.user_methods import UserMethods


class TestLoginUser:

    def test_post_login_user_existing_user_successfully(self):
        payload = data.EXISTING_USER
        user_methods = UserMethods()
        status_code, response_context = user_methods.post_login_user(payload)
        assert status_code == 200 and 'accessToken' in response_context

    @pytest.mark.parametrize(
        'email, password',
        [
            [helpers.create_random_email(), data.EXISTING_USER['password']],
            [data.EXISTING_USER['email'], helpers.generate_random_string(8)]
        ],
        ids=[
            'invalid email',
            'invalid password'
        ]
    )
    def test_post_login_user_with_some_invalid_data(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        user_methods = UserMethods()
        status_code, response_context = user_methods.post_login_user(payload)
        assert status_code == 401 and response_context["message"] == data.INVALID_DATA_MESSAGE

    @pytest.mark.parametrize(
        'email, password',
        [
            ['', data.EXISTING_USER['password']],
            [data.EXISTING_USER['email'], '']
        ],
        ids=[
            'empty email field',
            'empty password field'
        ]
    )
    def test_post_login_user_without_some_required_data(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        user_methods = UserMethods()
        status_code, response_context = user_methods.post_login_user(payload)
        assert status_code == 401 and response_context["message"] == data.INVALID_DATA_MESSAGE
