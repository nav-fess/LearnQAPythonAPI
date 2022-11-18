import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertion import Assertion

@allure.epic("Registration cases")
class TestUserRegister(BaseCase):
    @allure.description("This test check create user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user", data=data)

        Assertion.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexspected response " \
                                                                      f"content {response.content} "

    @allure.description("This test check create user with not existing email")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user", data=data)
        Assertion.assert_code_status(response, 200)
        Assertion.assert_json_has_key(response, "id")
