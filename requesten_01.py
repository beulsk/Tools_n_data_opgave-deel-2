import requests
import json
import re
import yaml
from pprint import pprint



import requests

api_base_url = "https://gitlab.com/api/v4"

response = requests.get(f"{api_base_url}/broadcast_messages")

response_data = response.json()
pprint(response_data)




