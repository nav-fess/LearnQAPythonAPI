from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertion import Assertion


class TestUserRegister(BaseCase):
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("api/user", data=data)

        Assertion.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexspected response " \
                                                                      f"content {response.content} "

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("api/user", data=data)
        Assertion.assert_code_status(response, 200)
        Assertion.assert_json_has_key(response, "id")
