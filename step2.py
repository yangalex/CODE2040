import requests

challenge_endpoint = "http://challenge.code2040.org/api/reverse"
result_endpoint = "http://challenge.code2040.org/api/reverse/validate"
token = "746dee53080c7af0f79e202c946b4216"

r = requests.post(challenge_endpoint, data={'token': token})
response_str = r.text

print("{}: got string {}".format(r.status_code, response_str))

# uses extended slice syntax to reverse (https://docs.python.org/2/whatsnew/2.3.html#extended-slices)
reversed_str = response_str[::-1]

r = requests.post(result_endpoint, data={'token': token, 'string': reversed_str})

print("sent string: {}".format(reverse_str))
