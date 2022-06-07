
conteo =0;
import time

estado_actual='A'
while True:
    entrada=input("Digite entrada (D1,D2): ")
    if (estado_actual=='A'):
        if (entrada=='D1'):
            estado_siguiente='B'
        elif (entrada=='D2'): estado_siguiente='C' #que permanezca en C  
        else: estado_siguiente='A' #En caso de un error, debe permanecer en el mismo estado
    elif (estado_actual=='B'): 
        if (entrada=='D1'): estado_siguiente='B'
        elif (entrada=='D2'): 
            estado_siguiente='A'
            conteo = conteo+1;
        else: estado_siguiente='B' #En caso de un error, debe permanecer en el mismo estado
    elif (estado_actual=='C'):
        if (entrada=='D1'): 
            estado_siguiente='A'
            if(conteo==0):
                print("Error no pueden salir automoviles porque aún no ha entrado ninguno")
            else:
                conteo = conteo-1;
        elif (entrada=='D2'): estado_siguiente='C'
        else: estado_siguiente='C'
    else:
        print("Error. Estado inválido")
    #actualización de estado actual, debido a la transición
    estado_actual=estado_siguiente
    print("Cantidad de vehiculos en el parqueadero: ",conteo);
    time.sleep(1) #retardo
