import time
import RPi.GPIO as GPIO
pins=[18,23,24,25,26]
pinb=[26,25,24,23,18]
GPIO.setmode(GPIO.BCM)
for i in pins:
    GPIO.setup(i,GPIO.OUT)
try:
    while True:
        for i in pins:
            GPIO.output(i,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(i,GPIO.LOW)
            time.sleep(0.5)
        for i in pins:
            GPIO.output(i,GPIO.HIGH)
            time.sleep(0.1)
        for i in pinb:
            GPIO.output(i,GPIO.LOW)
            time.sleep(0.1)
        for i in pins:
            GPIO.output(i,GPIO.HIGH)
        time.sleep(2)
        for i in pinb:
            GPIO.output(i,GPIO.LOW)
        time.sleep(2)
except  KeyboardInterrupt:
    for i in pins:
        GPIO.output(i, GPIO.LOW)
    for i in  pinb:
        GPIO.output(i, GPIO.LOW)
    GPIO.cleanup()
