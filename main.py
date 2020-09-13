from coretemp import CoreTemps
import requests


URL = "https://httpbin.org/post"


ct = CoreTemps()

# to json for send
core_temps_json = ct.get_json()

# for json to print


# POST on server
r = requests.post(URL, json= core_temps_json)

if r.status_code == 200:
	print("Posted on: " + URL)
	print(r.text)
# insignifact change on testing branch

