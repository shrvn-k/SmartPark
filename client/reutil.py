import re

def isMobileNo(num):
	rule = re.compile("\d{3}\d{3}\d{4}")
	if not rule.match(num):
		return False
	else: return True

def isEmail(email):
	rule =  re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
	if not rule.match(email):
		print 'vvvvvvvxcv'
		return False
	else: return True

def removeSpace(plate):
	newPlate = []
	for i in plate:
		if i != ' ':
			newPlate.append(i)
	lplate = ''.join(newPlate)
	return lplate.upper()






