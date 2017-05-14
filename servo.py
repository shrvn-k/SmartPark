'''
Servo angles:

0, 0.5ms, 2.5%
90, 1.5ms, 7.5%
180, 2.5ms, 12.5%

'''

import RPi.GPIO as GPIO
import time


servopin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin,GPIO.OUT)
servo = GPIO.PWM(servopin,50)
servo.start(7.5)

def gatepass():
	servo = GPIO.PWM(servopin,50)
	servo.start(7.5)
	print "Opening gate"
	servo.ChangeDutyCycle(2.5)
	print "Gate opened, Waiting"
	time.sleep(5)
	print "Closing gate"
	servo.ChangeDutyCycle(7.5)
	print "Gate closed"
	servo.stop()

