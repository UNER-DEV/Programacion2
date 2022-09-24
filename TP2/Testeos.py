#Objetos instanciados, según los puntos 1,2 y 3:
from Humano import *
from Monstruo import *
from MonstersInc import *

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

sullivan = Monstruo('James P. Sullivan', 'leon')
mike = Monstruo('Mike Wazowski', 'ciclope')
boo = Humano('Boo')
sullivan2 = Monstruo('James P. Sullivan', 'leon')
empresaMonster = MonstersInc()
empresaMonster.agregarHumano(boo)
empresaMonster.agregarMonstruo(mike)
empresaMonster.agregarMonstruo(sullivan)
empresaMonster.obtenerHumanos()
empresaMonster.obtenerMonstruos()
#sullivan2.establecerEnergia(75)
#empresaMonster.agregarMonstruo(sullivan2)
#boo.establecerEstadoAsustado(True)
#empresaMonster.agregarMonstruo(boo)
#empresaMonster.eliminarMonstruo(boo)
#empresaMonster.obtenerMonstruoByEnegia(101)
#empresaMonster.obtenerMonstruoByEnegia(80)