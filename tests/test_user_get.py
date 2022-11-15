import requessts
from lib.base_case import BaseCase
from lib.assertion import Assertion

class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):
        responce = requessts.get("https://playground.learnqa.ru/api/user/2")

        Assertion.assert_json_has_key(responce, "username")
        Assertion.assert_json_has_not_key(responce, "email")
        Assertion.assert_json_has_not_key(responce, "firstName")
        Assertion.assert_json_has_not_key(responce, "lastName")
