'''
            Raspberry Pi GPIO Pinout:

              3.3V |1   2| 5V
             GPIO2 |3   4| 5V
             GPIO3 |5   6| GND
    858764servo    GPIO4 |7   8| GPIO14 
               GND |9  10| GPIO15 
         d2 GPIO17 |11 12| GPIO18 d3
            GPIO27 |13 14| GND
         d4 GPIO22 |15 16| GPIO23 d1
              3.3V |17 18| GPIO24 e
            GPIO10 |19 20| GND
             GPIO9 |21 22| GPIO25 rs
            GPIO11 |23 24| GPIO8
               GND |25 26| GPIO7
             ID_SD |27 28| ID_SC
             GPIO5 |29 30| GND
             GPIO6 |31 32| GPIO12
            GPIO13 |33 34| GND
            GPIO19 |35 36| GPIO16 echo
     buzzer GPIO26 |37 38| GPIO20 trig
               GND |39 40| GPIO21

'''

import time 
import pigpio
from gpiozero import DistanceSensor, Buzzer, Servo
from RPLCD import CharLCD
from RPi import GPIO


#LCD Display
lcd = CharLCD(pin_rs=25,
              pin_e=24,
              pins_data=[23, 17, 18, 22],
              numbering_mode=GPIO.BCM,
              cols=16, rows=2,
              auto_linebreaks=True)

#Buzzer
BUZZER_PIN = 26
bz = Buzzer(BUZZER_PIN)

#Ultrasonic sensor
ECHO_PIN = 16
TRIGGER_PIN = 20
MAX_DIST = 2
ultrasonic = DistanceSensor(echo = ECHO_PIN, trigger = TRIGGER_PIN, max_distance = MAX_DIST)

'''
#Servo
servopin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin,GPIO.OUT)
servo = GPIO.PWM(servopin,50)
'''

#Servo pigpio
servopin = 4
GATE_OPEN = 1500
GATE_CLOSE = 500
pi = pigpio.pi()


def buzz(ontime = 0.5, offtime = 0.1, num = 2):
        bz.beep(on_time = ontime, off_time = offtime, n = num)

        
def isCar(dist = 60):
    distance = round(ultrasonic.distance*100,2)
    #print distance
    if distance < dist:
	return True
    else:
        return False


def enterPIN():
    confirm = False
    while not confirm:
        lcd.clear()
        lcd.write_string('Gatepass error!\n\rEnter PIN')
        pin = raw_input('Enter PIN')
        lcd.clear()
        lcd.write_string('Confirm PIN? Y/N\n\r')
        lcd.write_string(pin)
        choice = raw_input('Confirm PIN? Y/N')
        if choice.lower() == 'y':
            lcd.clear()
            lcd.write_string('PIN confirmed')
            confirm = True
    return pin


def reEnterPIN():
    confirm = False
    while not confirm:
        lcd.clear()
        lcd.write_string('Invalid PIN!\n\rRe-enter PIN')
        pin = raw_input('Enter PIN')
        lcd.clear()
        lcd.write_string('Confirm PIN? Y/N\n\r')
        lcd.write_string(pin)
        choice = raw_input('Confirm PIN? Y/N')
        if choice.lower() == 'y':
            lcd.clear()
            lcd.write_string('PIN confirmed')
            confirm = True
    return pin

def enterPIN(reEnter = False):

    confirm = False
    if reEnter == False:
        msg = 'Gatepass error!\n\rEnter PIN'
    else : msg = 'Invalid PIN!\n\rRe-enter PIN'
    
    while not confirm:
        lcd.clear()
        lcd.write_string(msg)
        pin = raw_input('Enter PIN: ')
        lcd.clear()
        #lcd.write_string('Confirm PIN? Y/N\n\r')
        lcd.write_string(pin)
        #choice = raw_input('Confirm PIN? Y/N')
        #if choice.lower() == 'y':
        #    lcd.clear()
        #    lcd.write_string('PIN confirmed')
        confirm = True
    return pin


'''
def gatepass(gatewait=10):
	#Servo
    servo = Servo(4)
    servo.max()
    print "Gate opened"
    time.sleep(3)
    print "Gate closing"
    servo.min()
    print "Gate closed"
    time.sleep(0.1)
    


def opengate():
	servo.min()


def closegate():
	servo.max()

'''


'''
def gatepass():
        servo.start(2.5)
        time.sleep(0.5)
        print "Opening gate"
        servo.ChangeDutyCycle(7.5)
        print "Gate opened, Waiting"
        time.sleep(5)
        print "Closing gate"
        servo.ChangeDutyCycle(2.5)
        time.sleep(2)
        print "Gate closed"
        servo.stop()
'''

def gatepass():
        print "Opening gate"
        pi.set_servo_pulsewidth(servopin,GATE_OPEN)
	time.sleep(3)
	print "Closing Gate"
	pi.set_servo_pulsewidth(servopin,GATE_CLOSE)
