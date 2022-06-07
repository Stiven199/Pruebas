from gpiozero import LEDBoard
from signal import pause
from time import sleep



leds= LEDBoard(17,27,22,4,5,6,13,19)
while True:
    for led in leds:
        led.on()
        sleep(1)
        led.off()