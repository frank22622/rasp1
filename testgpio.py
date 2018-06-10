import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(17, RPi.GPIO.OUT)

while True:
	RPi.GPIO.output(17, True)
	time.sleep(1)
	RPi.GPIO.output(17, False)
	time.sleep(1)
