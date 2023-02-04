import RPi.GPIO as GPIO
import time
import os

motion_pin = 23
buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    while True:
        if(GPIO.input(motion_pin) == 0):
            print("No movement...")
        elif(GPIO.input(motion_pin) ==1):
             print("Intruder detected! Capturing video...")
             GPIO.output(buzzer_pin, GPIO.HIGH)
             time.sleep(2)
             GPIO.output(buzzer_pin, GPIO.LOW)
             ts = int(time.time())
             os.system("ffmpeg -t  5 -f v4l2 -framerate 60 -video_size 1280x720 -i /dev/video0 /home/pi/Desktop/SourceCode/%s.avi" % ts)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
