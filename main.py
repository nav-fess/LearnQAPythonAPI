import requests
def print_text_api(link):
    response = requests.get(link)
    print(response.text)


link_hello = "https://playground.learnqa.ru/api/hello"
print_text_api(link_hello)
link_get_text = "https://playground.learnqa.ru/api/get_text"
print_text_api(link_get_text)
