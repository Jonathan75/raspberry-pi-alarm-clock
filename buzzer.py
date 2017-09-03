import time
from gpiozero import LED, PWMLED, Button

buzzer = PWMLED(17)
button = Button(21)


while (button.is_pressed != True ):
	buzzer.value = 1
	time.sleep(.5)
	buzzer.value = 0
	time.sleep(2)
