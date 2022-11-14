import requests
from requests import Response


def test_assert_text():
    text = str(input("Set a phrase: "))
    assert len(text) < 15, "phrase exceeds 15 characters"


def test_value_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    assert "HomeWork" in response.cookies, f"Cannot find cookie with name HomeWork in the last response"
    cookie = response.cookies.get('HomeWork')
    assert cookie == "hw_value", f"{cookie} not math with 'hw_value'"
