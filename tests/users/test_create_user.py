import pytest

import data
import helpers
from methods.user_methods import UserMethods


class TestCreateUser:

    def test_post_create_user_new_user_create_successfully(self):
        payload = {
            "email": helpers.create_random_email(),
            "password": helpers.generate_random_string(8),
            "name": helpers.generate_random_string(8)
        }
        user_methods = UserMethods()
        status_code, response_context = user_methods.post_create_user(payload)
        user_methods.delete_user(response_context['accessToken'])
        assert status_code == 200 and response_context['accessToken']

    def test_post_create_user_impossible_create_two_user_with_same_login(self):
        payload = data.EXISTING_USER
        user_methods = UserMethods()
        status_code, response_context = user_methods.post_create_user(payload)
        assert status_code == 403 and response_context["message"] == data.ALREADY_EXISTING_USER_MESSAGE

    @pytest.mark.parametrize(
        'email, password, name',
        [
            ['', helpers.generate_random_string(8), helpers.generate_random_string(8)],
            [helpers.create_random_email(), '', helpers.generate_random_string(8)],
            [helpers.create_random_email(), helpers.generate_random_string(8), '']
        ],
        ids=[
            'empty email field',
            'empty password field',
            'empty name field'
        ]
    )
    def test_post_create_user_without_some_required_data(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        user_methods = UserMethods()
        status_code, response_context = user_methods.post_create_user(payload)
        assert status_code == 403 and response_context["message"] == data.EMPTY_REQUIRED_FIELDS_MESSAGE
