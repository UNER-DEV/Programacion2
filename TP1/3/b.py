# Escribir un programa que resuelva la secuencia de Fibonacci a pedido del usuario. Deberá codificar una función fibonacci(numero), 
# cuyo parámetro numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio anterior, validado. 
# La función debe encargarse de calcular la secuencia para dicho número.

from modules.utils import *
import re

def fibonacci_recursiva(numero):
    if (numero<2):
        return numero
    return fibonacci_recursiva(numero-1)+fibonacci_recursiva(numero-2)

clear()
# Bucle para probar el programa varias veces
while True:
    msg = checkInputSiNo('\nDesea hacer la secuencia de Fibonacci?')
    if msg == "si":
        clear()
        # Ingreso de datos por el usuario
        while True:
            entrada = input("Ingrese un numero entero 'n' para hacer la secuencia de Fibonacci de 0 hasta 'n': ")
            if (len(re.findall(r'\d',entrada)) != len(entrada)) and int(entrada) < 0:
                print("Error: el numero ingresado no es valido\n\n")
            else:
                break
        print(f"Valor final: {fibonacci_recursiva(int(entrada))}")
    else:
        break





    