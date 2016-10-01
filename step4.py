import requests
import json

challenge_endpoint = "http://challenge.code2040.org/api/prefix"
response_endpoint = "http://challenge.code2040.org/api/prefix/validate"
token = "746dee53080c7af0f79e202c946b4216"

r = requests.post(challenge_endpoint, data={'token': token})
response = r.json()

prefix = response["prefix"]

# uses python list comprehensions to simplify loop
no_prefix = [elem for elem in response["array"] if not elem.startswith(prefix)]

data = {'token': token, 'array': no_prefix}
# note: had to use json= parameter in order to convert strings to json acceptable format
r = requests.post(response_endpoint, json=data)
print("{}: {}".format(r.status_code, r.text))