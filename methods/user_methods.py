import allure
import requests

from data import BASE_URL, CREATE_USER_URL, LOGIN_USER_URL, DELETE_USER_URL


class UserMethods:

    @allure.step('Метод создания нового пользователя - POST-запрос')
    def post_create_user(self, payload):
        response = requests.post(f'{BASE_URL}{CREATE_USER_URL}', json=payload)
        return response.status_code, response.json()

    @allure.step('Метод логина пользователя в системе - POST-запрос')
    def post_login_user(self, payload):
        response = requests.post(f'{BASE_URL}{LOGIN_USER_URL}', json=payload)
        return response.status_code, response.json()

    @allure.step('Метод удаления пользователя - DELETE-запрос')
    def delete_user(self, token):
        response = requests.delete(f'{BASE_URL}{DELETE_USER_URL}', headers={'Authorization': token})
        return response.status_code, response.json()

    @allure.step('Метод изменения данных пользователя - PATCH-запрос')
    def patch_update_user_data(self, payload, token):
        response = requests.patch(f'{BASE_URL}{DELETE_USER_URL}', headers={'Authorization': token}, json=payload)
        return response.status_code, response.json()
