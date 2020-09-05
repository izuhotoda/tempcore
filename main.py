import subprocess
import re
import json
import requests
from datetime import datetime

URL = "https://httpbin.org/post"

# capture sensors
proc = subprocess.Popen("sensors", stdout = subprocess.PIPE, stderr= subprocess.PIPE)
stdout, stderr = proc.communicate()

# bytes to string
temp_raw = stdout.decode("utf-8")
#print(temp_raw)

# parsing whit regex
pattern = re.compile(r'(\w+):\s+(.\d+.\d+).C\b')
matches = pattern.finditer(temp_raw)

# make a dict
core_temps = {'time': str(datetime.now())}
for match in matches:
	core_temps[match.group(1)] = float(match.group(2))
	
# to json for send
core_temps_json = json.dumps(core_temps)
# for json to print


# POST on server
r = requests.post(URL, json= core_temps_json)

if r.status_code == 200:
	print(datetime.now())
	print("Posted on: " + URL)
	print(json.dumps(core_temps, indent=4))
# insignifact change on testing branch