from Humano import *
from Monstruo import *
from modules.utils import *

class Puerta():

    # método de inicialización
    def __init__(self, num, hum):
        if(hum and type(hum) == Humano):
            self.__numero = num 
            self.__humano = hum
            self.__monstruo = None
            self.__estadoActiva = False
        else:
            print(f'Se intento conectar a algo distinto que un Humano')
    
    # comandos
    def establecerHumano(self, hum):
        if(hum and type(hum) == Humano):
            self.__humano = hum
        else:
            print(f'Se intento setear a algo distinto que un Humano')
    
    def establecerMonstruo(self, mon):
        print(type(mon))
        if(mon and type(mon) == Monstruo):
            self.__monstruo = mon
        else:
            print(f'Se intento setear a algo distinto que un Monstruo')
    
    def establecerEstadoActiva(self, est):
        self.__estadoActiva = est

    #consultas
    def obtenerNumero(self):
        return self.__numero

    def obtenerHumano(self):
        return self.__humano

    def obtenerMonstruo(self):
        return self.__monstruo

    def obtenerEstadoActiva(self):
        return self.__estadoActiva

    def obtenerEstadoEnUso(self):
        return self.__estadoActiva and self.__monstruo and type(self.__monstruo) == Monstruo
    #Se realiza comparación de identidad (igualdad superficial)
    def equals(self, puerta):
        return self.__numero == puerta.obtenerNumero() and self.__estadoActiva == puerta.obtenerEstadoActiva() and self.__humano == puerta.obtenerHumano() and self.__monstruo == puerta.obtenerMonstruo()