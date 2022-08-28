# Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2) que tome ambas como parámetros e
#  imprima dos listas, cada una con:
# i. Los elementos en común, en orden inverso.
# ii. Los elementos no comunes, en orden alfabético.
# El programa debería arrojar el siguiente resultado:
# listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
# ['c', 'b']
# ['a', 'e', 'd']

from modules.utils import *
clear()

def listas_diferencia(lista1, lista2):
    listas = lista1+lista2
    repetidos = sorted(obtenerRepetidos(listas),reverse=True)
    no_repetidos = sorted([i for i in listas if i not in repetidos])
    print(f"Las listas son: {lista1},{lista2}")
    print(f"Las letras repetidas: {repetidos}")
    print(f"Las letras no repetidas: {no_repetidos}")


#Test:
# listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
