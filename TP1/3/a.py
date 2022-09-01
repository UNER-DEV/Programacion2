from os import system
import re

def suma(numero):
    total = 0
    for i in range(1,int(numero)+1):
        total += i
    return total

system("cls")
#bucle para probar el programa varias veces
while True:
    if str(input("Desea hacer una suma?('s' o 'n'): ")).lower() == "s":
        system("cls")
        #ingreso de datos por el usuario
        while True:
            entrada = input("Ingrese un numero entero 'n' para hacer la sumatoria de 1 hasta 'n': ")
            if len(re.findall(r'\d',entrada)) != len(entrada):
                print("Error: el numero ingresado no es valido")
            else:
                break
        print(suma(entrada))
    else:
        break

