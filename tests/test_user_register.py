import requests
from lib.base_case import BaseCase
from lib.assertion import Assertion
from datetime import datetime

class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"


    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email,
        }

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertion.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unesxpected response " \
                                                                                               f"content {response.content} "

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email,
            }

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)
        Assertion.assert_code_status(response, 200)
        Assertion.assert_json_has_key(response, "id")

