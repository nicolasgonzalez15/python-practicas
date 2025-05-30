#Funcion factorial
def factorialNro(n):
  resultado = 1
  for i in range(1, n + 1):
    resultado *= i
  return resultado

#Inicializo variable continua juego en true
continua = True

#Bucle while - Mientras se pueda continuar ingresando nros. positivos
while continua:

    #Ingreso valor 
    valor = input("Ingrese un número entero mayor a 0: ")

    if(valor.isdigit()):
        #Convierto valor a número entero
        nroIngresado = int(valor)
        if(nroIngresado>0):
        #Ingreso de frase
            #continua = True
            frase= input("Ingrese una frase: ")
            print(f"Frase ingresada: {frase}")

            #Cuento caracteres de frase
            caracteresFrase = len(frase)
            print(f"Cantidad de caracteres de la frase: {caracteresFrase}")

            #Calculo factorial con caracteres de frase
            factorialFrase = factorialNro(caracteresFrase)
            print(f"Factorial de caracteres de frase: {factorialFrase}")

            #Resultado par o impar
            if(factorialFrase%2==0):
                print("El resultado del factorial de la frase es PAR.")
            else:
                print("El resultado del factorial de la frase es IMPAR.")

        else:
            print("Error. El número debe ser mayor a 0.")
            continua = False
            
       
    else:
        print("Caracteres inválidos. Por favor ingrese un número.")
        continua = False

#Aviso de fin de juego
print("Finalizó el juego.")