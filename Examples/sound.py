import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

#define sound pin
sound_pin = 24
#set GPIO mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)
#setup pin as INPUT
GPIO.setup(sound_pin, GPIO.IN)

class LCDModule():
    def __init__(self):
        #Define LCD column and row size for 16x2 LCD
        self.address = 0x21
        self.lcd_columns = 16
        self.lcd_rows = 2
        #Initialize the LCD using pins
        self.lcd = LCD.Adafruit_CharLCDBackpack(address = self.address)

    def turn_off(self):
         #Turn backlight off
         self.lcd.set_backlight(1)

    def turn_on(self):
        #Turn backlight on
        self.lcd.set_backlight(0)

    def clear(self):
        #clear the LCD screen
        self.lcd.clear()

    def write_lcd(self, text):
        #turn on LCD
        self.turn_on()
        #wait 0.1 seconds
        time.sleep(0.1)
        #Print a two line message
        self.lcd.message(text)
        #wait 3 seconds
        time.sleep(3)
        #clear the screen
        self.clear()
        #wait 0.1 seconds
        time.sleep(0.1)
        #turn off LCD
        self.turn_off()

#define LCD module
lcd_screen = LCDModule()
try:
    while True:
        #check if sound detected or not
        #the sound pin always HIGH unless sound detected, it goes LOW
        if(GPIO.input(sound_pin) == True):
            #sound detected, print sound detected for 3  seconds
            lcd_screen.write_lcd(text = "Sound Detected!")
            #sleep for 0.1 seconds before continue
            time.sleep(0.1)
        else:
            #no sound detected turn off  LCD
            lcd_screen.clear()
            lcd_screen.turn_off()
except KeyboardInterrupt:
    #CTRL+C detected, cleaning and quiting the script
    lcd_screen.clear()
    lcd_screen.turn_off()
    GPIO.cleanup()
