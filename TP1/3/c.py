# Tal como sucede con la lógica proposicional, en Python muchas veces las expresiones booleanas pueden ser simplificadas manteniendo
# el valor de verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente a a and b.
# A continuación, intente simplificar las siguientes expresiones y escriba un procedimiento procesar_sentencias(a, b, c) 
# que permita evaluar el valor de verdad de las expresiones ya simplificadas:

## SIMPLIFICACIÓN DE LAS EXPRESIONES:
# i. (a or b) or (b and c)
#    a or (b or (b and c))
#    a or b
#
# ii. b and c or False
#     b and c
#
# iii. a and b or c or (b and a)
#      a and b or (b and a) or c
#      a and (b or (b and a)) or c
#      a and b or c
#
# iv. a == True or b == False
#     a or b'

from modules.utils import *

def procesar_sentencias(a, b, c):
    print("i.    (a or b) or (b and c)    => Resultado: %s" % (a or b))
    print("ii.      b and c or False      => Resultado: %s" % (b and c))
    print("iii. a and b or c or (b and a) => Resultado: %s" % (a and b or c))
    print("iv.   a == True or b == False  => Resultado: %s" % (a or not b))

def entrada_de_usuario():
    while True:
        entrada = input(">> Ingrese 1 (True) o 0 (False): ")
        if entrada != '0' and entrada != '1' :
            print("Error: ingreso incorrecto")
        else:
            break
    clear()
    return entrada == '1'

clear()
#bucle para probar el programa varias veces
while True:
    msg = checkInputSiNo('\nDesea ingresar valores para evaluar las expresiones booleanas?')
    if msg == "si":
        clear()
        #ingreso de datos por el usuario
        print("1er entrada:")
        entrada1 = entrada_de_usuario()
        print("2da entrada:")
        entrada2 = entrada_de_usuario()
        print("3er entrada:")
        entrada3 = entrada_de_usuario()
        print("|     a = " + str(entrada1) + "   |   b = " + str(entrada2) + "   |   c = " + str(entrada3) + "     |")
        procesar_sentencias(entrada1,entrada2,entrada3)
    else:
        break

