import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

print ("Running...")    

try:
    while True:
        file = open("./signals/table01_signal", "r")
        status = int(file.read())
        file.close()
    #    print (status)
        if status == 0:
            GPIO.output(17, False)
            GPIO.output(18, False)
        elif status == 1:
            GPIO.output(17, True)
            GPIO.output(18, False)
        elif status == 2:
            GPIO.output(17, False)
            GPIO.output(18, True)
    #   time.sleep(2)
  
except KeyboardInterrupt:  
    print ("\nLights terminated")
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.cleanup()
  
except:  
    print ("Other error or exception occurred")
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.cleanup()
  
else:
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.cleanup()
