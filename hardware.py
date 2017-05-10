import time 
from gpiozero import DistanceSensor, Buzzer
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
