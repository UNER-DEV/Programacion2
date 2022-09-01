import re
import time
from funciones import *

# ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
while True:
    edad = input("Ingrese su edad: ")
    if len(re.findall(r'\d',edad)) != len(edad):
        print("Error: edad ingresada no es valida")
    else:
        break
# seteo inicial de variables
hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = calculo_edad_en_dias(hora_local, anio_comienzo, anio_fin)
# imprimir la edad del usuario
print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d días" % (meses, dias))