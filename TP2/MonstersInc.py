from Humano import *
from Monstruo import *

class MonsterInc():
    # método de inicialización
    def __init__(self):
        self.__monstruos = [] 
        self.__humanos = []
    
    # comandos
    def agregarMonstruo(self,monstruo):
        #verificar Obj de tipo monstruo
        self.__monstruos.append(monstruo)
    def agregarHumano(self,hum):
        #verificar Obj de tipo humano
        self.__humanos.append(hum)
    def eliminarMonstruo(self,monstruo):
        #verificar Obj de tipo monstruo
        self.__monstruos.remove(monstruo)
    def eliminarHumano(self,hum):
        #verificar Obj de tipo humano
        self.__humanos.remove(hum)

    #consultas
    def obtenerMonstruos(self):
        #realizar for para impresión de los objetos
        return self.__monstruos
    def obtenerHumanos(self):
        #realizar for para impresión de los objetos
        return self.__humanos

sullivan = Monstruo('James P. Sullivan', 'leon')
mike = Monstruo('Mike Wazowski', 'ciclope')
boo = Humano('Boo')
sullivan2 = Monstruo('James P. Sullivan', 'leon')
empresaMonster= MonsterInc()
empresaMonster.agregarHumano(boo)
empresaMonster.agregarMonstruo(mike)
empresaMonster.agregarMonstruo(sullivan)
print(empresaMonster.obtenerMonstruos())
print(empresaMonster.obtenerHumanos())