from gpiozero import LEDBoard
from signal import pause
from time import sleep



leds= LEDBoard(17,27,22,4)
# leds2= LEDBoard(17,27,22,4)
while True:
    print("Menú de usuario")
    print("1. Giro horario")
    print("2. Giro antihorario")
    print("3. Medio paso horario")
    print("4. Medio paso antihorario")
    seleccion = int (input())
    t = float(input("Ingrese el tiempo entre cada paso"))
    if seleccion== 1:
        for led in leds:
            led.on()
            sleep(t)
            led.off()
    elif seleccion == 2:
            for i in range(3,0,-1):
                leds[i].on()
                sleep(t)
                leds[i].off()
    elif seleccion ==3:
        leds.value=(1,0,0,0)
        sleep(t)
        leds.value=(1,1,0,0)
        sleep(t)
        leds.value=(0,1,0,0)
        sleep(t)
        leds.value=(0,1,1,0)
        sleep(t)
        leds.value=(0,0,1,0)
        sleep(t)
        leds.value=(0,0,1,1)
        sleep(t)
        leds.value=(0,0,0,1)
        sleep(t)
        leds.value=(1,0,0,1)
        sleep(t)
        
    elif seleccion ==4:
        leds.value=(1,0,0,1)
        sleep(t)
        leds.value=(0,0,0,1)
        sleep(t)
        leds.value=(0,0,1,1)
        sleep(t)
        leds.value=(0,0,1,0)
        sleep(t)
        leds.value=(0,1,1,0)
        sleep(t)
        leds.value=(0,1,0,0)
        sleep(t)
        leds.value=(1,1,0,0)
        sleep(t)
        leds.value=(1,0,0,0)
        sleep(t)
    else:
        print("error")