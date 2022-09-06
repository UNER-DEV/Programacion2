# A continuación, se presenta el código de un programa que, ante la edad ingresada por el usuario, este presenta el equivalente en días, meses y años. Se solicita al alumno que lo refactorice de manera tal que:
    # a. Se elimine la sentencia if / else de la función anio_bisiesto.
    # b. Las múltiples sentencias if la función dia_mes utilicen la cláusula in en lugar de varias cláusulas or.
    # c. Se agregue una sentencia que valide que la edad ingresada por el usuario es numérica.
    # d. Se agregue una función que encapsule el cálculo del equivalente de la edad en días y que tome como parámetros las variables hora_local, anio_comienzo y anio_fin.

import re
import time
# Las funciones modificadas se encuentran en la carpeta utils, bajo el nombre calendar.py. 
# Para seguir con la misma estructura previa, decidimos trasladarlo allí.
from modules.utils import *

clear()
# Ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
while True:
    edad = input("Ingrese su edad: ")
    if len(re.findall(r'\d',edad)) != len(edad):
        print("Error: edad ingresada no es valida")
    else:
        break

# Seteo inicial de variables
hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = calculo_edad_en_dias(hora_local, anio_comienzo, anio_fin)

# Imprimir la edad del usuario
print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d dias" % (meses, dias))