from urllib.request import urlopen
import time
"""
@Ahmed_Salama
This is a simple function that checks the internet connection by sending request to Google server.
If server is reachable, then it means that the internet is up and running.
"""
def internet_on():
	# Increase the time period
	try_time = 1
	while True:
		try:
			urlopen('http://172.217.19.142', timeout=1)
			print("Internet is up!")
			time.sleep(5)

		except:
			x = try_time
			while x:
				#\r (Carriage Return) - 
				#moves the cursor to the beginning of the (same) line without advancing to the next line
				print("Reconnect in %d sec." %x, end="\r")
				time.sleep(1)
				x -= 1
			try_time = try_time * 2

if __name__ == "__main__":
	internet_on()
