import RPi.GPIO as GPIO
import time

try:
    number = 0
    while True:
        number = number + 1
        print(number)
        time.sleep(1)
except KeyboardInterrupt:
    exit()


