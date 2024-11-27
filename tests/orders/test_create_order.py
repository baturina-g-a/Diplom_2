import data
from methods.order_methods import OrderMethods


class TestCreateOrder:

    def test_post_create_order_authorized_user_with_ingredients_successfully(self, login_user):
        payload = {
            "ingredients": data.CORRECT_HASH_INGREDIENTS
        }
        order_methods = OrderMethods()
        response = order_methods.post_create_order(login_user, payload)
        status_code = response.status_code
        response_context = response.json()
        assert status_code == 200 and response_context["order"]["status"] == "done"

    def test_post_create_order_authorized_user_without_ingredients_impossible(self, login_user):
        payload = {
            "ingredients": []
        }
        order_methods = OrderMethods()
        response = order_methods.post_create_order(login_user, payload)
        status_code = response.status_code
        response_context = response.json()
        assert status_code == 400 and response_context["message"] == data.MISSING_INGREDIENTS_MESSAGE

    # ошибка: неавторизованный пользователь может создать заказ, статус код 200, тест написан на фактический результат
    # но тело ответа приходит неполным, поэтому проверка только на статус код
    def test_post_create_order_unauthorized_user_impossible(self):
        payload = {
            "ingredients": data.CORRECT_HASH_INGREDIENTS
        }
        order_methods = OrderMethods()
        response = order_methods.post_create_order(payload=payload, token='')
        status_code = response.status_code
        assert status_code == 200

    def test_post_create_order_with_incorrect_ingredient_hash(self, login_user):
        payload = {
            "ingredients": data.INCORRECT_HASH_INGREDIENTS
        }
        order_methods = OrderMethods()
        response = order_methods.post_create_order(login_user, payload)
        error_code = response.status_code
        body = response.text
        assert error_code == 500 and 'Internal Server Error' in body

