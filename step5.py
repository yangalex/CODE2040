import requests
import json
import dateutil.parser
import datetime
import string

challenge_endpoint = "http://challenge.code2040.org/api/dating"
response_endpoint = "http://challenge.code2040.org/api/dating/validate"
token = "746dee53080c7af0f79e202c946b4216"

r = requests.post(challenge_endpoint, data={'token': token})
response = r.json()
interval = response["interval"]

# convert timestamp to datetime object
timestamp = dateutil.parser.parse(response["datestamp"])

# add interval using timedelta
timestamp = timestamp + datetime.timedelta(0, interval)
timestamp = timestamp.isoformat().replace("+00:00", "Z")

r = requests.post(response_endpoint, data={'token': token, 'datestamp': timestamp})
print("{}: {}".format(r.status_code, r.text))