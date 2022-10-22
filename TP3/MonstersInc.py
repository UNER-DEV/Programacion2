from Humano import *
from Monstruo import *
from modules.utils import *

# class MonstersInc():
#     # método de inicialización
#     def __init__(self):
#         self.__monstruos = [] 
#         self.__humanos = []
    
#     # comandos
#     def agregarMonstruo(self,monstruo):
#         if(type(monstruo) == Monstruo):
#             self.__monstruos.append(monstruo)
#         else:
#             print('Se intento agregar un objeto que no es Monstruo')

#     def agregarHumano(self,hum):
#         if(type(hum) == Humano):
#             self.__humanos.append(hum)
#         else:
#             print('Se intento agregar un objeto que no es Humano')

#     def eliminarMonstruo(self, monstruo):
#         if(type(monstruo) == Monstruo):
#             self.__monstruos.remove(monstruo)
#         else:
#             print('Se intento eliminar un objeto que no es Monstruo')

#     def eliminarHumano(self,hum):
#         if(type(hum) == Humano):
#             self.__humanos.remove(hum)
#         else:
#             print('Se intento eliminar un objeto que no es Humano')

#     #consultas
#     def obtenerMonstruos(self):
#         self.obtenerMonstruosByFiltro('','')
    
#     def obtenerHumanos(self):
#         self.obtenerHumanosByFiltro('','')

#     #Servicio generalizado para no repetir codigo
#     def obtenerHumanosByFiltro(self,filtro,value):
#         result = []
#         for hum in self.__humanos:
#             if(filtro == 'Estado'):
#                 if(hum.obtenerEstadoAsustado() == value):
#                     result.append(hum)
#             #En caso de no haber filtro
#             else:
#                 result.append(hum)
#         clear()
#         if(len(result) == 0):
#             print('No se encontraron Humanos')
#         else:
#             for hum in result:
#                 print(hum)
    
#     #Servicio generalizado para no repetir codigo
#     def obtenerMonstruosByFiltro(self,filtro,value):
#         result = []
#         for mon in self.__monstruos:
#             if(filtro == 'Energia'):
#                 if(mon.obtenerEnergia() < value):
#                     result.append(mon)
#             elif(filtro == 'Especie'):
#                 if(mon.obtenerEspecie() == value):
#                     result.append(mon)
#             #En caso de no haber filtro
#             else:
#                 result.append(mon)
#         clear()
#         if(len(result) == 0):
#             print('No se encontraron Monstruos')
#         else:
#             for mon in result:
#                 print(mon)
    
#     def obtenerMonstruosByEspecie(self,value):
#         self.obtenerMonstruosByFiltro('Especie',value)

#     def obtenerMonstruosByEnegia(self,value):
#         self.obtenerMonstruosByFiltro('Energia',value)

#     def obtenerHumanosByEstado(self,value):
#         self.obtenerHumanosByFiltro('Estado',value)

#Modificaciones a la clase Monstruo segun punto 4
class MonstersInc():
    # método de inicialización
    def __init__(self):
        self.__monstruos = [] 
        self.__puertas = []
    
    # comandos
    def agregarMonstruos(self,monstruos):
        if(type(monstruos.get("asustador")) == Monstruo and type(monstruos.get("asistente")) == Monstruo):
            if(monstruos.get("asustador").obtenerPareja() == monstruos.get("asistente") and monstruos.get("asistente").obtenerPareja() == monstruos.get("asustador")):
                self.__monstruos.append(monstruos)
            else:
                print('Los monstruos no son pareja')
        else:
            print('Se intento agregar un objeto que no es una pareja de Monstruos')

    def agregarPuerta(self, pue):
        if(type(pue) == Puerta):
            self.__puertas.append(pue)
        else:
            print('Se intento agregar un objeto que no es Puerta')

    def eliminarMonstruos(self,monstruos):
        if(type(monstruos.get("asustador")) == Monstruo and type(monstruos.get("asistente")) == Monstruo ):
            self.__monstruos.remove(monstruos)
        else:
            print('Se intento eliminar un objeto que no es una pareja de Monstruos')

    def eliminarPuerta(self, pue):
        if(type(pue) == Puerta):
            self.__puertas.remove(pue)
        else:
            print('Se intento eliminar un objeto que no es una Puerta')

    #consultas
    def obtenerMonstruos(self):
        self.obtenerMonstruosByFiltro('','')
    
    def obtenerPuertas(self):
        print(self.__puertas)
    
    #Servicio generalizado para no repetir codigo
    def obtenerMonstruosByFiltro(self,filtro,value):
        result = []
        for mon in self.__monstruos:
            if(filtro == 'Energia'):
                if(mon.obtenerEnergia() < value):
                    result.append(mon)
            elif(filtro == 'Especie'):
                if(mon.obtenerEspecie() == value):
                    result.append(mon)
            #En caso de no haber filtro
            else:
                result.append(mon)
        clear()
        if(len(result) == 0):
            print('No se encontraron Monstruos')
        else:
            for mon in result:
                print(mon)
    
    def obtenerMonstruosByEspecie(self,value):
        self.obtenerMonstruosByFiltro('Especie',value)

    def obtenerMonstruosByEnegia(self,value):
        self.obtenerMonstruosByFiltro('Energia',value)