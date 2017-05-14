# import hardware.hardware as hw
import hardware.hardwaredummy as hw
import controller as cont
import querystring as qr
import ast

def senseAlways():

	while True:
		with open('meta.txt') as f:
			di = f.read()
			di = ast.literal_eval(di)
			isReg = di['isReg']
			# isSense = di['isSense']
			print 'isReg = ',isReg 
			if not isReg:
				vehicleDetect = hw.isCar()
				if vehicleDetect:
					cont.control_gate_pass()

if __name__ == '__main__':
	senseAlways()
