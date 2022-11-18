import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertion import Assertion

@allure.epic("User edit cases")
class TestUserEdit(BaseCase):
    @allure.description("This test create user")
    def test_edit_just_create_user(self):
        # REGISTR
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("api/user", data=register_data)

        Assertion.assert_code_status(response1, 200)
        Assertion.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Change Name"

        response3 = MyRequests.put(
            f"api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertion.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertion.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )
