from Humano import *
from Monstruo import *

class MonsterInc():
    # método de inicialización
    def __init__(self):
        self.__monstruos = [] 
        self.__humanos = []
    
    # comandos
    def agregarMonstruo(self,monstruo):
        if(type(monstruo) == Monstruo):
            self.__monstruos.append(monstruo)
        else:
            print('Se intento agregar un objeto que no es Monstruo')

    def agregarHumano(self,hum):
        if(type(hum) == Humano):
            self.__humanos.append(hum)
        else:
            print('Se intento agregar un objeto que no es Humano')

    def eliminarMonstruo(self,monstruo):
        if(type(monstruo) == Monstruo):
            self.__monstruos.remove(monstruo)
        else:
            print('Se intento eliminar un objeto que no es Monstruo')

    def eliminarHumano(self,hum):
        if(type(hum) == Humano):
            self.__humanos.remove(hum)
        else:
            print('Se intento eliminar un objeto que no es Humano')

    #consultas
    def obtenerMonstruos(self):
        self.obtenerMonstruosByFiltro('','')
    
    def obtenerHumanos(self):
        self.obtenerHumanosByFiltro('','')

    #Servicio generalizado para no repetir codigo
    def obtenerHumanosByFiltro(self,filtro,value):
        for hum in self.__humanos:
            if(filtro == 'Estado'):
                if(hum.obtenerEstadoAsustado() == value):
                    print(hum)
            #En caso de no haber filtro
            else:
                print(hum)
    
    #Servicio generalizado para no repetir codigo
    def obtenerMonstruosByFiltro(self,filtro,value):
        for mon in self.__monstruos:
            if(filtro == 'Energia'):
                if(mon.obtenerEnergia() < value):
                    print(mon)
            elif(filtro == 'Especie'):
                if(mon.obtenerEspecie() == value):
                    print(mon)
            #En caso de no haber filtro
            else:
                print(mon)
    
    def obtenerMonstruoByEspecie(self,value):
        self.obtenerMonstruosByFiltro('Especie',value)

    def obtenerMonstruoByEnegia(self,value):
        self.obtenerMonstruosByFiltro('Energia',value)

    def obtenerHumanosByEstado(self,value):
        self.obtenerHumanosByFiltro('Estado',value)

sullivan = Monstruo('James P. Sullivan', 'leon')
mike = Monstruo('Mike Wazowski', 'ciclope')
boo = Humano('Boo')
sullivan2 = Monstruo('James P. Sullivan', 'leon')
empresaMonster = MonsterInc()
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