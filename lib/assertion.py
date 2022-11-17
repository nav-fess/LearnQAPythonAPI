from requests import Response
import json

class Assertion:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_at_dict = response.json()
        except json.JSONDecoderError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        assert name in response_at_dict, f"response json doesn`t have key '{name}'"
        assert response_at_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name ):
        try:
            response_at_dict = response.json()
        except json.JSONDecoderError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        assert name in response_at_dict, f"response json doesn`t have key '{name}'"


    @staticmethod
    def assert_json_has_keys(response: Response, names):
        try:
            response_at_dict = response.json()
        except json.JSONDecoderError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        for name in names:
            assert name in response_at_dict, f"response json doesn`t have key '{name}'"


    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_at_dict = response.json()
        except json.JSONDecoderError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        assert name not in response_at_dict, f"response json should n`t have key '{name}' But it`s present"


    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"Unexpected status code! Expected: {expected_status_code}." \
                                                             f"Actual {response.status_code}"
