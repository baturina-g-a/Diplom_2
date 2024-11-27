import allure

import data
from methods.order_methods import OrderMethods


class TestGetUserOrdersList:

    @allure.title('Проверка получения списка заказов конкретного авторизованного пользователя')
    @allure.description('Проверяем, что после авторизации в тело ответа возвращается список заказов, статус ответа 200')
    def test_get_orders_list_for_authorized_user_successfully(self, login_user):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.get_orders_list(login_user)
        assert status_code == 200 and type(order_methods.get_orders_list(login_user)[1]["orders"]) == list

    @allure.title('Проверка, что невозможно получить список заказов для неавторизованного пользователя')
    @allure.description('Проверяем, что, если пользователь не авторизации, то список заказов получить невозможно, '
                        'получаем: статус ответа 401 и сообщение о необходимости авторизоваться')
    def test_get_orders_list_for_unauthorized_user_impossible(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.get_orders_list(token='')
        assert status_code == 401 and response_context["message"] == data.UNAUTHORIZED_USER_MESSAGE
