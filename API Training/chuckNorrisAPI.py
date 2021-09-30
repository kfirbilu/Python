import requests
import json


url = "https://api.chucknorris.io/jokes/random"

# headers = {'accept': "application/json"} # can work w/out

# querystring = {"query":"<REQUIRED>"}  # only if its a written query (search)

# response = requests.request("GET", url,headers=headers,querystring = querystring)

response = requests.request("GET", url)

with open('test.json', 'w') as f:
    f.write(str(response.text))

res = json.loads(response.text)
print(response.text)
print(res.get('value'))
