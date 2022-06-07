
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT)

p = GPIO.PWM(36,50) 
p.start(50)
while True:
    ciclo = input("Ingrese el ciclo util deseado:\n")
    frecuencia = input("Ingrese la frecuencia deseada:\n")
    p.ChangeDutyCycle(int(ciclo))
    p.ChangeFrequency(int(frecuencia))
    sleep(5)
    