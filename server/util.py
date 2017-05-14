import random
import string
import datetime as dt

def genrate_pin(pinRange = 6):
	code = list()
	for i in range(pinRange):
	    code.append(random.choice(string.digits))

	return ''.join(code)

def get_current_date_time():
	# return '18-4-2017'
	currDate = dt.datetime.now()
	return currDate

if __name__ == "__main__":
	# pin = genrate_pin()
	# print type(pin)
	# print pin
	print get_current_date_time()
	pass
