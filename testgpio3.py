import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while True:
	nb = int(input('Key 1 to on, 0 to off, 2 to quit: '))
	if nb == 1:
		GPIO.output(18, False)
		GPIO.output(17, True)
		nb = int(input('Now Key 1 to switch, 2 to quit: '))
		if nb == 1:
                        GPIO.output(17, False)
                        GPIO.output(18, True)
	if nb == 0:
		GPIO.output(17, False)
	if nb == 2:
		break

GPIO.output(17, False)
GPIO.output(18, False)
GPIO.cleanup()
