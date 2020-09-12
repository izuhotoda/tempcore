'''

+ write sensors
+ asking about vars
+ show Json
'''
import subprocess
import re
import json
from datetime import datetime

class CoreTemps():

	def __init__(self):
		'''
		Setting vars to be included in json packages
		'''	
		flag = True
		while flag:
			# print sensors out
			proc = subprocess.Popen("sensors", stdout = subprocess.PIPE, stderr= subprocess.PIPE)
			stdout, stderr = proc.communicate()
			print (stdout.decode("utf-8"))

			# witchcores
			self.key_cores = input ("witch cores? : ")
			

			# for json to print
			print (self.__get_cores(stdout, prettify=True))

			# it's ok?
			accept_json = input("Json template is ok? [N/y]").lower()

			if (accept_json == "y"):
				flag = False
			print("---------------------------")
	
	def get_json(self, prettify = False):
		'''
		get json
		'''
		proc = subprocess.Popen("sensors", stdout = subprocess.PIPE, stderr= subprocess.PIPE)
		stdout, stderr = proc.communicate()
		if prettify:
			return self.__get_cores(stdout, prettify=True)
		else:
			return self.__get_cores(stdout)


	def __get_cores(self, stdout, prettify=False):
		'''
		parser and composer
		'''
		cores_pattern = self.key_cores + r'(\w*\s*\d*):\s+(.\d+.\d+)'
		# parsing whit regex
		pattern = re.compile(cores_pattern)
		#pattern = re.compile(r'(\w+):\s+(.\d+.\d+).C\b')
		matches = pattern.finditer(stdout.decode("utf-8"))
		# make a dict
		core_temps = {'time': str(datetime.now())}
		#core_temps = {}
		for match in matches:
			core_temps[self.key_cores + match.group(1)] = float(match.group(2))
		# to json for send
		if prettify:
			return json.dumps(core_temps, indent=4)
		else:
			return json.dumps(core_temps)



if __name__ == "__main__":
	ct = CoreTemps()
	print(ct.get_json())



