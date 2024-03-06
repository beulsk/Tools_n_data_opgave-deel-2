"""
Opdracht:

Bepalingen:
 - Je moet gebruik maken van de aangeleverde variable(n)
 - Je mag deze variable(n) niet aanpassen
 - Het is de bedoeling dat je op het einde 1 programma hebt
 - Als inlever formaat wordt een public git url verwacht die gecloned kan worden

/ 5 ptn 1 - Maak een public repository aan op jouw gitlab/github account voor dit project
/10 ptn 2 - Gebruik python om de gegeven joke_url aan te spreken
/10 ptn 3 - Gebruik regex om de volgende data te extracten:
            - De eerste 20 tekens van de joke
/15 ptn 4 - Verzamel onderstaande data en output alles als yaml. Een voorbeeld vind je hieronder.
/10 ptn 5 - Doe een post naar de post_url.
            - Stuur in de post een parameter genaamd "naam" mee met als waarde jouw voornaam
            - Output het hele antwoord naar de terminal
            - Haal uit het antwoord van de call jouw ip adres (origin) en geef dit weer met een f string

Totaal  /50ptn
"""

""" voorbeeld yaml output
jokes:
  - intro: <met regex extracted intro>
    joke: <joke>
    id: <joke id>
  - .. <tot aantal jokes bereikt is>
"""

# https://httpbin.org/#/HTTP_Methods/post_post
post_url = "https://httpbin.org/post"

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

    volledige_info_joke = requests.get(joke_url, headers=headers).json()

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
    
print(yaml.dump(totaal))
pprint(totaal[2])

data = {
    'name' : 'Codedamn'
}

response = requests.post("https://httpbin.org/post", data)
print(response.text)

