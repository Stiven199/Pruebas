
import time
#normalmente, se debe asignar un estado inicial del sistema
estado_actual='Apagada'
while True:
    L= input("Digite estado de L(0 o 1)")
    entrada=input("Digite entrada (Detener,Encender,Lavar,Puerta): ")
    if (estado_actual=='Apagada'):
        if ((entrada=='Encender') & (L=="1")):
            estado_siguiente='Encendida'
        elif (entrada=='Detener'): estado_siguiente='Apagada' #que permanezca Apagada  
        elif (entrada=='Lavar'): estado_siguiente='Apagada' #que permanezca Apagada 
        elif (entrada=='Puerta'): estado_siguiente='Apagada' #que permanezca Apagada 
        else: estado_siguiente='Apagada' #En caso de un error, debe permanecer en el mismo estado
    elif (estado_actual=='Encendida'): 
        if ((entrada=='Lavar') & (L=="1")): estado_siguiente='Lavando'
        elif (entrada=='Detener'): estado_siguiente='Encendida' #que permanezca Encendida
        elif (entrada=='Encender'): estado_siguiente='Encendida' #que permanezca Encendida
        elif ((entrada=='Puerta') & (L=="1")): estado_siguiente='Apagada' #que se Apague
        else: estado_siguiente='Encendida' #En caso de un error, debe permanecer en el mismo estado
    elif (estado_actual=='Lavando'):
        if ((entrada=='Puerta') & (L=="1")): estado_siguiente='Apagada' #que se apague
        elif ((entrada=='Detener') & (L=="1")): estado_siguiente='Encendida' #que cambie de estado a encendida
        elif (entrada=='Encender'): estado_siguiente='Lavando' # que permanezca lavando
        elif (entrada=='Lavar'): estado_siguiente='Lavando' # que permanezca lavando
        else: estado_siguiente='Lavando'                    # que permanezca lavando
    
    else:
        print("Error. Estado inválido")
    #actualización de estado actual, debido a la transición
    estado_actual=estado_siguiente
    print("Estado actual: ",estado_actual)
    time.sleep(1) #retardo
