import requests
def print_text_api(link, params = ""):
    response = requests.get(link, params)
    print(response.text)

payload = { "name": " "}
link_hello = "https://playground.learnqa.ru/api/hello"
print_text_api(link_hello, payload)
link_get_text = "https://playground.learnqa.ru/api/get_text"
print_text_api(link_get_text)
