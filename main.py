from coretemp import CoreTemps
import requests
import json

URL = "https://httpbin.org/post"
#URL = "http://192.168.100.8:8000/api/"


ct = CoreTemps()

# to json for send
core_temps_json = ct.get_json()

# POST on server
r = requests.post(URL, data= json.dumps({'name':'i7'}))
print(r.headers.get('Content-Type'))

if r.status_code == 200:
	print("Posted on: " + URL)
	print(r.text)
	print(r.json()['json'])
# insignifact change on testing branch