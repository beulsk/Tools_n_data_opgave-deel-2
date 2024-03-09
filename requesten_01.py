en nu vanaf hier

en nu vanaf de PC

import requests
import json

import re
import yaml
from pprint import pprint

payload = {"name": "Mike", "age": "25"}

# response = requests.post("https://httpbin.org/post", data=payload)

headers = {
    "User-Agent"
}

response = requests.get("https://httpbin.org/user-agent")
# print(response.url)

# if response.status_code ==  requests.codes.not_found:
#     print("not found")
# else:
#     print(response.status_code)

print (response.text)

# res_jason = response.json()

# pprint(res_jason)
