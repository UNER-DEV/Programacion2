# Escribir una función de nombre palabra_no_tiene_letras(palabra, letras_prohibidas), 
# la cual retorne True si es que los caracteres que componen una palabra no se encuentran en una lista de caracteres prohibidos.

from modules.utils import *
clear()

def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in letras_prohibidas:
        if normalizar(letra) in normalizar(palabra):
            print("El programa retorna False")
            return False
    print("El programa retorna True")
    return True   



#Test:
#palabra_no_tiene_letras("GatO", ["u","b","e"])