from coretemp import CoreTemps
import requests
import json

URL = "https://httpbin.org/post"


ct = CoreTemps()

# to json for send
core_temps_json = ct.get_json()

# POST on server
r = requests.post(URL, json= core_temps_json)

if r.status_code == 200:
	print("Posted on: " + URL)
	print(r.text)
	print(r.json()['json'])
# insignifact change on testing branch