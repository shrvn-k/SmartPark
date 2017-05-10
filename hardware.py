'''
            Raspberry Pi GPIO Pinout:

              3.3V |1   2| 5V
             GPIO2 |3   4| 5V
             GPIO3 |5   6| GND
             GPIO4 |7   8| GPIO14 servo
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

#Servo
servo = Servo(14)


def buzz(duration = 2):
        bz.beep(on_time = duration, n = 1)

        
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


def openGate(gatewait=10):
    servo.mid()
    time.sleep(gatewait)
    servo.min()