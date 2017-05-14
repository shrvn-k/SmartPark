from time import *

def buzz(duration = 2):
        # bz.beep(on_time = duration, n = 1)
        print ('Buzzzzzz!!!')

        
def isCar(dist = 60):
    sleep(1)
    return True


# def enterPIN(reEnter = False):

#     confirm = False
#     if reEnter == False:
#         msg = 'Gatepass error!\n\rEnter PIN'
#     else : msg = 'Invalid PIN!\n\rRe-enter PIN'
    
#     while not confirm:
#         lcd.clear()
#         lcd.write_string(msg)
#         pin = raw_input('Enter PIN')
#         lcd.clear()
#         lcd.write_string('Confirm PIN? Y/N\n\r')
#         lcd.write_string(pin)
#         choice = raw_input('Confirm PIN? Y/N')
#         if choice.lower() == 'y':
#             lcd.clear()
#             lcd.write_string('PIN confirmed')
#             confirm = True
#     return pin

def enterPIN(reEnter = False):
	confirm = False
	if reEnter == False:
		msg = 'Gatepass error!'
	else : msg = 'Invalid PIN!'

	print msg
	pin = raw_input('Eneter PIN : ')
	return pin

def gatepass(gatewait=10):
    print 'open boom barier'
    sleep(1)
    print 'close boom barrier'


    


