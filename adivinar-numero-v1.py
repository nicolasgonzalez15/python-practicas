import random

nroSecreto = random.randint(1,20)

incorrecto = True
intentos = 1

while incorrecto and intentos<=5:
    
    valorIngresado = input("Ingresar número entre 1 y 20: ")
    
    #Valido si se ingresan números o caracteres
    if(valorIngresado.isdigit()):
        #Convierto valor a entero
        nroIngresado = int(valorIngresado)

        #Valido que esté en el rango solicitado
        if(1<=nroIngresado<=20):
               #Valido si es igual, menor o mayor
            if(nroIngresado == nroSecreto):
                incorrecto = False
        
        #Incremento número de intentos SOLO si es número en el rango
            elif  (nroIngresado<nroSecreto):
                print("El número ingresado es menor al número secreto")
                intentos+=1
            else:
                print("El número ingresado es mayor al número secreto")
                intentos+=1
        #Fuera de rango  
        else:
            print("Fuera de rango. Debe ingresar números enteros entre 1 y 20. Vuelva a intentar nuevamante.")
    #Valor no numérico
    else:
        print("Caracteres no válidos. Debe ingresar números enteros entre 1 y 20. Vuelva a intentar nuevamante.")

if(incorrecto==False):
    print(f"Felicitaciones! Usted adivinó el número secreto!")

if(intentos>5):
    print(f"Usted no acertó el número secreto. El número era: {nroSecreto}")