import hardware as hw

hw.buzz(duration)
Rings buzzer for given duration
Params:
	duration: time to buzz, default = 2

hw.isCar(dist)
Returns true if car is between 0 and dist centimeters from sensor.
Params:
	dist: max dist of vehicle, default = 60

hw.enterPIN()
Prompts for PIN on the LCD display and returns the entered PIN.

hw.reEnterPIN()
In case PIN entry fails first time. Call this. Same as enterPIN() but 
message displayed is different.

hw.openGate(duration)
Opens the boom-barrier and closes it after a pre-defined duration.
Params:
	duration: duration between opening and closing in seconds, default = 10

