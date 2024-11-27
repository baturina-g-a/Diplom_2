BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
CREATE_USER_URL = 'auth/register'
LOGIN_USER_URL = 'auth/login'
DELETE_USER_URL = 'auth/user'
ORDERS_URL = 'orders'

EXISTING_USER = {
    "email": "bga14@yandex.ru",
    "password": "password1",
    "name": "username1"
}

CORRECT_HASH_INGREDIENTS = ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa74", "61c0c5a71d1f82001bdaaa6c"]
INCORRECT_HASH_INGREDIENTS = ["aaaaaaa", "bbbbbbb", "cccccc"]

INVALID_DATA_MESSAGE = 'email or password are incorrect'
ALREADY_EXISTING_USER_MESSAGE = 'User already exists'
EMPTY_REQUIRED_FIELDS_MESSAGE = 'Email, password and name are required fields'
UNAUTHORIZED_USER_MESSAGE = 'You should be authorised'

MISSING_INGREDIENTS_MESSAGE = 'Ingredient ids must be provided'
