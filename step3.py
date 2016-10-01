import requests
import json

challenge_endpoint = "http://challenge.code2040.org/api/haystack"
results_endpoint = "http://challenge.code2040.org/api/haystack/validate"
token = "746dee53080c7af0f79e202c946b4216"

r = requests.post(challenge_endpoint, data={'token': token})
response = r.json()

needle_index = -1
for index, elem in enumerate(response["haystack"]):
  if elem == response["needle"]:
    needle_index = index

if needle_index != -1:
  r = requests.post(results_endpoint, data={'token': token, 'needle': needle_index})

print(r.status_code)
