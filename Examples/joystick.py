import time
import spidev

#Open SPI bus
spi = spidev.SpiDev()
spi.open(0,1)
spi.max_speed_hz = 1000000

def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel) << 4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

x_channel = 1
y_channel = 0
delay = 0.15

try:
    while True:
        x_value = ReadChannel(x_channel)
        y_value = ReadChannel(y_channel)
        if x_value > 650:
            print("Left")
        if x_value < 400:
            print("Right")
        if y_value  >  650:
            print("Up")
        if y_value < 400:
            print("Down")
        time.sleep(delay)
except KeyboardInterrupt:
    exit()
