import allure
import requests

from data import BASE_URL, ORDERS_URL


class OrderMethods:

    @allure.step('Метод создания заказа - POST-запрос')
    def post_create_order(self, token, payload):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', headers={'Authorization': token}, json=payload)
        return response

    @allure.step('Метод получения списка заказов конкретного пользователя - GET-запрос')
    def get_orders_list(self, token):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}', headers={'Authorization': token})
        return response.status_code, response.json()
