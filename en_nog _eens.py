joke_url = "https://icanhazdadjoke.com"
amount_of_jokes = 5

import requests
import json
import re
import yaml
from pprint import pprint

url = "https://icanhazdadjoke.com"
headers = {"Accept": "application/json"}

getal  = None
twintig_eerste_dict = []
output = []
totaal = []

for aantal in range(amount_of_jokes):

    volledige_info_joke = requests.get(url, headers=headers).json()

    id_joke = volledige_info_joke['id']
    # print(id_joke)
    joke_gedeelte = volledige_info_joke['joke']
    regex_joke_gedeelte = r"(^(?P<zoekintro>[A-Za-z0-9\s\W]{20}))"

    for match in re.finditer(regex_joke_gedeelte,joke_gedeelte):
        twintig_eerste_dict = match.groupdict()
        
    twintig_eerste = (twintig_eerste_dict["zoekintro"])

# print(twintig_eerste)
# print(" ")
# print(joke_gedeelte) 
# print(" ")
# print(id_joke)
    
        
    output = {
    "intro": twintig_eerste,
    "joke": joke_gedeelte,
    "id": id_joke 
    }

    totaal.append(output.copy())
else:
    print(" ")

    
print(yaml.dump(totaal))