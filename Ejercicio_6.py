while True:
    print("");
    print("Simulacion Tabla de Verdad");
    a= int(input("Digite el valor de a"));
    b= int(input("Digite el valor de b"));
    c= int(input("Digite el valor de c"));
    if(a==0):
        a=False;
    else:
        a=True;
    if(b==0):
        b=False;
    else:
        b=True;    
    if(c==0):
        c=False;
    else:
        c=True;    
    if(a==0 and b==0 and c==1):
        S = 1;
        print("El resultado de la operacion es : S=1 Verdadero");
    elif(a==0 and b==1 and c==1):
            S = 1;
            print("El resultado de la operacion es : S=1 Verdadero");
    elif(a==1 and b==0 and c==0):
            S = 1;
            print("El resultado de la operacion es : S=1 Verdadero");
    elif(a==1 and b==1 and c==1):
            S = 1;
            print("El resultado de la operacion es : S=1 Verdadero");
    else:
            S = 0;
            print("El resultado de la operacion es : S=0 Falso");
    print("");
   