import random

nroSecreto = random.randint(1,20)
print(f"Numero secreto: {nroSecreto}")
incorrecto = True
intentos = 1

while incorrecto and intentos<=5:
    valorIngresado = input("Ingrsar número entre 1 y 20: ")
    
    #Valido si se ingresan números o caracteres
    if(valorIngresado.isdigit()):
        nroIngresado = int(valorIngresado)
    else:
        print("Error. Debe ingresar números enteros entre 1 y 20. Vuelva a intentar nuevamante.")
        break

    #Valido que sea entre 1 y 20
    if not(1<=nroIngresado<=20):
        print("Error. Debe ingresar números enteros entre 1 y 20. Vuelva a intentar nuevamante.")
        break

    #Valido si es igual, menor o mayor
    if(nroIngresado == nroSecreto):
        incorrecto = False
        #mensaje = "El número ingresado es correcto!"
    elif  (nroIngresado<nroSecreto):
        print("El número ingresado es menor al número secreto")
    else:
        print("El número ingresado es mayor al número secreto")
    
    #Incremento número de intentos
    intentos+=1

if(incorrecto==False):
    print(f"Felicitaciones! Usted adivinó el número secreto!")

if(intentos>5):
    print(f"Usted no acertó el número secreto. El número era: {nroSecreto}")