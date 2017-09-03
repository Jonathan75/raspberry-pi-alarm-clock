import time, datetime
from gpiozero import LED, PWMLED, Button

buzzer = PWMLED(17)
button = Button(21)

start = datetime.datetime.now()

def endtime():
	return (datetime.datetime.now()-datetime.timedelta(seconds=30)) 

def timeout():
	return endtime() > start

def still_alarm():
	if button.is_pressed:
		return False
	else:
		return (timeout() == False)	

while still_alarm()
	buzzer.value = 1
	time.sleep(.5)
	buzzer.value = 0
	time.sleep(2)


