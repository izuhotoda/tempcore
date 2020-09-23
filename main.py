from coretemp import CoreTemps
import requests
import json
from threading import Thread
from time import sleep

URL = "https://httpbin.org/post"
#URL = "http://192.168.100.8:8000/logger/api/"
#URL = "https://julia004.herokuapp.com/api/"

ct = CoreTemps()

# to json for send
def post(seconds):
	while True:
		core_temps_json = ct.get_dict()
		print(core_temps_json)
		# POST on server
		response = requests.post(URL, data= core_temps_json)
		if response.ok:
			print("Posted on: " + URL)
			print(response.text)
		else:
			print(response.status_code)
			print(response.raw)
		sleep(seconds)

# insignifact change on testing branch

t = Thread(target=post, args=(30,))
t.start()