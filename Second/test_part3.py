import requests
import pytest
from requests import Response

headers = [
    {"User-Agent":
         "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 "
        "(KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"
        "Expected values:'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'"},
    {"User-Agent":
         "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 "
         "(KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"
         "Expected values:'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'"},
    {"User-Agent":
         "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
         "Expected values:'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'"},
    {"User-Agent":
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
         "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"
         "Expected values:'platform': 'Web', 'browser': 'Chrome', 'device': 'No'"},
    {"User-Agent":
         "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15"
         "(KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'"
         "Expected values:'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'"},
]
'''
def test_assert_text():
    text = str(input("Set a phrase: "))
    assert len(text) < 15, "phrase exceeds 15 characters"


def test_value_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    assert "HomeWork" in response.cookies, f"Cannot find cookie with name HomeWork in the last response"
    cookie = response.cookies.get('HomeWork')
    assert cookie == "hw_value", f"{cookie} not math with 'hw_value'"


def test_value_header():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    assert "x-secret-homework-header" in response.headers, f"Cannot find cookie with name HomeWork in the last response"
    header = response.headers.get('x-secret-homework-header')
    assert header == "Some secret value", f"{header} not math with 'Some secret value '"  
    '''


@pytest.mark.parametrize("header", headers)
def test_user_agent(header):
    rezult = []

    response = requests.get(
        "https://playground.learnqa.ru/ajax/api/user_agent_check",
        headers=header).json()

    if response['device'] == 'Unknown': rezult.append('device')
    if response['platform'] == 'Unknown': rezult.append('platform')
    if response['browser'] == 'Unknown': rezult.append('browser')

    if len(rezult) != 0:
        print(f"header = {header} \n Void fields = {rezult} \n\n")
