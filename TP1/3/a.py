# a. Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo que numero = 10: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    # En el programa que invoque dicha función:
    # i. El usuario debe poder ingresar el valor del parámetro numero.
    # ii. Debe validarse que el dato ingresado por el usuario corresponda a un dígito, y no a otro tipo de dato como un carácter.
    # iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for, while).

from modules.utils import *
import re

def suma(numero):
    total = 0
    for i in range(1,int(numero)+1):
        total += i
    return total

## BONUS: Resolución recursiva.
def suma_recursiva(numero):
    if numero>0:
        return numero + suma_recursiva(numero-1)
    return numero

clear()
#bucle para probar el programa varias veces
while True:
    msg = checkInputSiNo('\nDesea hacer una suma?')
    if msg == "si":
        clear()
        #ingreso de datos por el usuario
        while True:
            entrada = input("Ingrese un numero entero 'n' para hacer la sumatoria de 1 hasta 'n': ")
            if len(re.findall(r'\d',entrada)) != len(entrada):
                print("Error: el numero ingresado no es valido\n")
            else:
                break
        #print(f"{suma(entrada)}\n\n")
        print(f"{suma_recursiva(int(entrada))}\n\n")
    else:
        break
