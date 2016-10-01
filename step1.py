import requests

r = requests.post("http://challenge.code2040.org/api/register",
                  data = {'token': '746dee53080c7af0f79e202c946b4216', 'github': 'https://github.com/yangalex/CODE2040'})

print(r.status_code)