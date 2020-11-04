from threading import Thread
import time
from random import uniform

def get_data(seconds):
	while True:
		time.sleep(seconds)
		print(time.ctime(time.time()), uniform(0,10))
		
t = Thread(target=get_data, args=(1,))
t.start()