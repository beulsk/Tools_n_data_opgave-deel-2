import requests
from pprint import pprint

# url = "https://www.example.com"
# antwoord = requests.get(url)

# print(antwoord.headers)

data ={"naam": "Karel"}
url = "https://httpbin.org/post"

antwoord = requests.post(url, json=data)

antwoord_data = antwoord.json()

pprint(antwoord_data)

# for vriend, kenmerken in vrienden.items():
#     for kenmerk, waarde in kenmerken.items():
#         print(f"{vriend} zijn {kenmerk} is {waarde}")

pst = antwoord_data['json']



print(f"dit werd gepost door {antwoord_data['json']['naam']}")
print(f"En mijn ip adres is {antwoord_data['origin']}")


