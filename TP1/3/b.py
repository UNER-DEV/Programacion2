from os import system
import re

def fibonacci(numero):
    if numero == 0:
        total = 0
    else:
        if numero == 1:
            total = 1
        else:
            a = 1
            b = 1
            for i in range(int(numero)-3):
                total = a + b
                b = a
                a = total
    return total

system("cls")
#bucle para probar el programa varias veces
while True:
    if str(input("Desea hacer la secuencia de Fibonacci?('s' o 'n'): ")).lower() == "s":
        system("cls")
        #ingreso de datos por el usuario
        while True:
            entrada = input("Ingrese un numero entero 'n' para hacer la secuencia de Fibonacci de 1 hasta 'n': ")
            if (len(re.findall(r'\d',entrada)) != len(entrada)) and int(entrada) >= 0:
                print("Error: el numero ingresado no es valido")
            else:
                break
        print(fibonacci(int(entrada)))
    else:
        break

