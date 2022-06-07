from gpiozero import PWMLED
from time import sleep
led = PWMLED(17)


while True:
    x =input("Ingrese el valor del retardo")
    for i in range(0,11,1):
        led.value = (i/10)
        sleep(int(x))
        print("valor pwm : ",i/10)
    y =input("Ingrese el valor del retardo")
    for i in range(40,-1,-10):
        led.value = (i/40)
        sleep(int(x))
        print("valor pwm : ",i/40)
    sleep(2)
    
    for i in range(0,5,1):
        led.value = (i/5)
        sleep(int(x))
        print("valor pwm : ",i/5)
   
    for i in range(5,-1,-1):
        led.value = (i/5)
        sleep(int(x))
        print("valor pwm : ",i/5)