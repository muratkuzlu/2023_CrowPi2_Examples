import RPi.GPIO as GPIO
import dht11
import time
import os

#initialize GPIO
instance = dht11.DHT11(pin = 4)
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

#main
try:
    result = instance.read()
    while result.is_valid():
        os.system('clear')
        time.sleep(0.1)
        print('Temp = {0:0.1f}*c\nHumd = {1:0.1f}%\n'.format(result.temperature, result.humidity))
        time.sleep(0.5)
        os.system('clear')
        time.sleep(0.1)

    if result.is_valid() == 0:
        print('Failed to get reading. Try again!')
except KeyboardInterrupt:
    GPIO.cleanup()


