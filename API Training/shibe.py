import requests
import json

count = 3

url = f"http://shibe.online/api/shibes?count={count}"

response = requests.request("get",url)

res = json.loads(response.text)

print(response.text)

print(res)
