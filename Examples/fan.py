import RPi.GPIO as GPIO

relay_pin = 21
touch_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setup(touch_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(touch_pin):
            GPIO.output(relay_pin, GPIO.HIGH)
        else:
            GPIO.output(relay_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.output(relay_pin, GPIO.LOW)
    GPIO.cleanup()
