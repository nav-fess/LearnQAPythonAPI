import time
import requests
import json


def fields_json(link_api, json_fields, params_request=None):
    response, responses = "", {}
    if params_request is None:
        response = requests.get(link_api)
    elif len(params_request) > 0:
        response = requests.get(link_api, params_request)
    else:
        return {"Error": "Void dict"}

    for field in json_fields:
        responses[field] = json.loads(response.text)[field]
    return responses


link = "https://playground.learnqa.ru/ajax/api/longtime_job"

fields = fields_json(link, ["token", "seconds"])
seconds, token = fields["seconds"], fields["token"]

params = {"token": token}
fields = fields_json(link, ["status"], params)
print(f"status = {fields['status']}")

if fields["status"] == "Job is NOT ready":
    time.sleep(int(seconds))
    fields = fields_json(link, ["status", "result"], params)
    print(f"status = { fields['status']}, result = {fields['result']}")
