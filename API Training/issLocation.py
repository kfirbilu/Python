import requests
import json

url = "https://api.wheretheiss.at/v1/satellites/25544"

response = requests.request("GET",url)

res = json.loads(response.text)

print(res)

long = 31.88719896762421

lat = 34.81386441772433

url = f"https://api.wheretheiss.at/v1/coordinates/{long},{lat}"

response2 = requests.request("GET",url)

res2 = json.loads(response2.text)

print(res2.get("map_url"))



