import RPi.GPIO as GPIO
import time

class sg90:
    def __init__(self, direction):
        self.pin = 19
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.direction = int(direction)
        self.servo = GPIO.PWM(self.pin, 50)
        self.servo.start(0.0)

    def cleanup(self):
        self.servo.ChangeDutyCycle(self._henkan(0))
        time.sleep(0.3)
        self.servo.stop()
        GPIO.cleanup()

    def currentdirection(self):
        return self.direction

    def _henkan(self, value):
        return 0.05 * value + 7.0

    def setdirection(self, direction, speed):
        for d in range(self.direction, direction, int(speed)):
            self.servo.ChangeDutyCycle(self._henkan(d))
            self.direction = d
            time.sleep(0.1)
        self.servo.ChangeDutyCycle(self._henkan(direction))
        self.direction = direction

#Configure the motor with sg90 class
s = sg90(0)
#Change direction
print("Turning Counter-clockwise")
s.setdirection(100, 80)
time.sleep(0.5)
print("Turning Clockwise")
s.setdirection(-100, 80)
time.sleep(0.5)
#Clean the motor
s.cleanup()
