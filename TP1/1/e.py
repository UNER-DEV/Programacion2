# Escribir un procedimiento numeros_par_impar(entrada) que, dada una lista de números, eleve cada elemento impar 
# en ella al cuadrado y los mueva a otra lista e imprima ambas. La lista de números la ingresa el usuario 
# en forma de números separados por coma.

# Suponiendo que el usuario ingresa la siguiente lista: [1,2,3,4,5,6,7,8,9]
# Entonces, la salida del programa debería ser:
# 2,4,6,8
# 1,9,25,49,81
from modules.utils import *
clear()

def numeros_par_impar(entrada):
    impares = []
    for num in entrada:
        if( not EsParOImpar(num)):
            impares.append(num**2)
            entrada.remove(num)
    print(f"Lista original sin los numeros impares: {entrada}")
    print(f"Nueva lista con los numeros impares: {impares}")


#Test:
#numeros_par_impar([1,2,3,4,5,6,7,8,9])