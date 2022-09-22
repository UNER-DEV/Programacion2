#Objetos instanciados, según los puntos 1,2 y 3:
from Humano import *
from Monstruo import *

sullivan = Monstruo('James P. Sullivan', 'leon')
mike = Monstruo('Mike Wazowski', 'ciclope')
boo = Humano('Boo')
sullivan2 = Monstruo('James P. Sullivan', 'leon')


print(sullivan.obtenerEnergia())
print(mike.obtenerEnergia())
print(boo.obtenerEstadoAsustado())
sullivan.asustar(boo)
print(sullivan.obtenerEnergia())
print(mike.obtenerEnergia())
print(boo.obtenerEstadoAsustado())
mike.divertir(boo)
print(sullivan.obtenerEnergia())
print(mike.obtenerEnergia())
print(boo.obtenerEstadoAsustado())