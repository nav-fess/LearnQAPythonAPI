import allure
import requests
from environment import ENV_OGJECT
from .logger import Logger


class MyRequests():
    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request for URL: {url}"):
            return MyRequests._send(url, data, headers, cookies, "GET")


    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"POST request for URL: {url}"):
            return MyRequests._send(url, data, headers, cookies, "POST")


    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"PUT request for URL: {url}"):
            return MyRequests._send(url, data, headers, cookies, "PUT")


    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"DELETE request for URL: {url}"):
            return MyRequests._send(url, data, headers, cookies, "DELETE")


    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):

        url = f"{ENV_OGJECT.get_base_url()}{url}"
        if headers is None: headers = {}
        if cookies is None: cookies = {}

        Logger.add_request(url, data, cookies, headers, method)

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        if method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        if method == 'PUT':
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        if method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            Exception(f"Bad HTTP method {method} was received")

        Logger.add_responce(response)

        return response
