import data
import helpers
from methods.user_methods import UserMethods


class TestUpdateUserData:

    def test_patch_update_authorized_user_data_successfully(self, create_and_delete_user):
        payload = {
            "email": helpers.create_random_email(),
            "password": helpers.generate_random_string(8),
            "name": helpers.generate_random_string(8)
        }
        user_methods = UserMethods()
        status_code, response_context = user_methods.patch_update_user_data(payload, create_and_delete_user)
        assert status_code == 200 and response_context['success'] is True

    def test_patch_update_unauthorized_user_data_impossible(self):
        payload = {
            "email": helpers.create_random_email(),
            "password": helpers.generate_random_string(8),
            "name": helpers.generate_random_string(8)
        }
        user_methods = UserMethods()
        status_code, response_context = user_methods.patch_update_user_data(payload, token='')
        assert status_code == 401 and response_context["message"] == data.UNAUTHORIZED_USER_MESSAGE
