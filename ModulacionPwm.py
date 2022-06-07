from gpiozero import PWMLED
from time import sleep
from signal import pause
led = PWMLED(17)

while True:
    
    led.value = 0.01
   