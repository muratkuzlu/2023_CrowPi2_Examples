import RPi.GPIO as GPIO
import time
import spidev
from rpi_ws281x import PixelStrip, Color

#LED strip configuration
LED_COUNT = 64  #Number of LED pixels
LED_PIN = 12    #GPIO pin connected
LED_FREQ_HZ = 800000   #LED signal frequency
LED_DMA = 10    #DMA channel to use
LED_BRIGHTNESS = 10 #LED brightness level
LED_INVERT = False  #LED not inverted
LED_CHANNEL = 0
#Open SPI bus
spi = spidev.SpiDev()
spi.open(0,1)
spi.max_speed_hz = 1000000
#Other Component Configuration
relay_pin = 21
buzzer_pin = 18
gas_channel = 7
#Input/Output setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

#Function for RGB Matrix
def colorWipe(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

#Function for Gas Sensor
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

#Main
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()
delay = 0.15
try:
    while  True:
        gas_value = ReadChannel(gas_channel)
        print(gas_value)
        time.sleep(delay)
        if gas_value < 500:
            GPIO.output(relay_pin, GPIO.LOW)
            GPIO.output(buzzer_pin, GPIO.LOW)
            colorWipe(strip, Color(0,255,0))
        elif gas_value >= 500 and gas_value < 700:
            GPIO.output(relay_pin, GPIO.LOW)
            colorWipe(strip, Color(100,64,0))
            for x in range(3):
                GPIO.output(buzzer_pin, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(buzzer_pin, GPIO.LOW)
        else:
            colorWipe(strip, Color(255,0,0))
            GPIO.output(relay_pin, GPIO.HIGH)
            GPIO.output(buzzer_pin, GPIO.HIGH)

except KeyboardInterrupt:
    GPIO.output(buzzer_pin, GPIO.LOW)
    GPIO.output(relay_pin, GPIO.LOW)
    colorWipe(strip, Color(0,0,0))
    GPIO.cleanup()
