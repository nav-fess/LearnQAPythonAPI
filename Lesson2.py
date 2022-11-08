import json
import requests

def print_part_json(obj_json):
    obj = json.loads(obj_json)
    return f"message[2] = {obj['messages'][1]['message']}"

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
#print(print_part_json(json_text))


def address_last_redirect(link):
    response = requests.get(link)
    return f"amount redirect = {len(response.history)} and last url = {response.url}"

link = "https://playground.learnqa.ru/api/long_redirect"
#print(address_last_redirect(link))

def requests_and_methods(link = "https://playground.learnqa.ru/ajax/api/compare_query_type"):
    params = {"name": "name"}
    response = requests.get(link, params=params)
    print(f"response = {response}")
    combinations_requests(link)
    return True

def combinations_requests(link):
    methods = ['POST', 'GET', 'PUT', 'DELETE']
    for method in methods:
        params = {'method': method}
        response = requests.get(link, params=params)
        print(f"GET | method = {method} | response = {response.text} | code = {response.content}")
        response1 = requests.post(link, data=params)
        print(f"POST | method = {method} | response = {response1.text} | code = {response1.content}")
        response2 = requests.put(link, data=params)
        print(f"PUT | method = {method} | response = {response2.text} | code = {response2.content}")
        response3 = requests.delete(link, data=params)
        print(f"DELETE | method = {method} | response = {response3.text} | code = {response1.content}")

print(requests_and_methods())

