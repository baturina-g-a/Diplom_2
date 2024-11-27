import allure
import pytest

import data
import helpers
from methods.user_methods import UserMethods


class TestLoginUser:

    @allure.title('Проверка логина существующего пользователя')
    @allure.description('Проверяем, что при заполнении всех обязательных полей происходит логин существующего '
                        'пользователя, получаем: код ответа 200 и тело ответа содержит accessToken')
    def test_post_login_existing_user_successfully(self):
        payload = data.EXISTING_USER
        user_methods = UserMethods()
        status_code, response_context = user_methods.post_login_user(payload)
        assert status_code == 200 and 'accessToken' in response_context

    @allure.title('Проверка, что невозможен логин пользователя с некорректным логином (email) или паролем')
    @allure.description('Проверяем, что если в поле логина/пароля ввести несоответствующее значение, то авторизация '
                        'не происходит, получаем: код ответа 401 и сообщение, что данные введены некорректно')
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

    @allure.title('Проверка, что невозможен логин пользователя с незаполненным логином (email) или паролем')
    @allure.description('Проверяем, что если оставить поле логина/пароля пустым, то авторизация не происходит, '
                        'получаем: код ответа 401 и сообщение, что данные некорректны')
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
