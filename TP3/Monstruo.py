from Humano import *
from Puerta import *

# class Monstruo():
#     max_energia = 100

#     # método de inicialización
#     def __init__(self, nombre, esp):
#         self.__nombre = nombre
#         self.__especie = esp
#         self.__energia = self.max_energia
#         self.__estadoDormido = False

#     # comandos
#     def establecerNombre(self, nombre):
#         self.__nombre = nombre
    
#     def establecerEspecie(self, esp):
#         self.__especie = esp
    
#     def establecerEnergia(self, energia):
#         if(energia >= 0 and energia < self.max_energia):
#             self.__energia = energia
#         elif(energia >= self.max_energia):
#             self.__energia = self.max_energia
#         else:
#             print(f'Se intento setear un valor de energia no valido, debe ser un valor positivo, siendo el valor maximo a setear {self.max_energia}')

#     #Se modificó el comando asustar y se añadió divertir
#     def asustar(self, hum):
#         if(not self.__estadoDormido):
#             if(hum and type(hum) == Humano):
#                 if(not hum.obtenerEstadoAsustado()):
#                     if(self.__energia - 10 >= 0):
#                         self.__energia -= 10
#                         hum.establecerEstadoAsustado(True)
#                     else:
#                         print(f'El monstruo no puede asustar porque no tiene energía')  
#                 else:
#                     print(f'El monstruo no puede asustar a un humano ya asustado')  
#             else:
#                 print(f'El monstruo no puede asustar a algo que no es humano')  
#         else:
#             print(f'El monstruo esta dormido') 
    
#     def divertir(self, hum):
#         if(not self.__estadoDormido):
#             if(hum and type(hum) == Humano):
#                 if(self.__energia - 20 >= 0):
#                     self.__energia -= 20
#                     hum.establecerEstadoAsustado(False)
#                 else:
#                     print(f'El monstruo no puede divertir porque no tiene energía')
#             else:
#                 print(f'El monstruo no puede divertir a algo que no es humano')  
#         else:
#             print(f'El monstruo esta dormido') 
    
#     def dormir(self):
#         if(self.__energia < self.max_energia):
#             self.establecerEnergia(self.__energia + 15)
#         else:
#             print(f'El monstruo ya tiene la energia completa') 

#     def despertar(self):
#         if(not self.__estadoDormido):
#             self.__estadoDormido = True
#         else:
#             print(f'El monstruo ya estaba despierto') 
    
#     #consultas
#     def obtenerNombre(self):
#         return self.__nombre

#     def obtenerEspecie(self):
#         return self.__especie

#     def obtenerEnergia(self):
#         return self.__energia

#     def __str__(self):
#         return '[El monstruo ' + str(self.__nombre) + ', de especie ' + str(self.__especie) + ', tiene ' + str(self.__energia) + ' de energia]'

#Modificaciones a la clase Monstruo segun punto 3
class Monstruo():
    max_energia = 100
    min_Energia = 15

    # método de inicialización
    def __init__(self, nombre, esp, tipo):
        if(tipo == 'asustador' or tipo == 'asistente'):
            self.__nombre = nombre
            self.__especie = esp
            self.__energia = self.max_energia
            self.__tipo = tipo
            self.__pareja = None
            self.__estadoDormido = False
        else:
            print(f'Se intento setear con un tipo incorrecto');

    # comandos
    def establecerNombre(self, nombre):
        self.__nombre = nombre
    
    def establecerEspecie(self, esp):
        self.__especie = esp
    
    def establecerEnergia(self, energia):
        if(energia >= 0 and energia < self.max_energia):
            self.__energia = energia
        elif(energia >= self.max_energia):
            self.__energia = self.max_energia
        else:
            print(f'Se intento setear un valor de energia no valido, debe ser un valor positivo, siendo el valor maximo a setear {self.max_energia}')

    def establecerPareja(self, mou):
        if(mou and type(mou) == Monstruo and mou.obtenerTipo() != self.__tipo):
            self.__pareja = mou
    
    def activarPuerta(self, pue, mou):
        if(self.__tipo == 'asistente'):
            if(pue and type(pue) == Puerta and mou and type(mou) == Monstruo):
                if(not pue.obtenerEstadoEnUso()):
                    pue.establecerEstadoActiva(True)
                    pue.establecerMonstruo(mou)
                    #Se decide dejar establecido a la pareja debido a que es el que entra en la puerta
                else:
                    print(f'La puerta ya esta siendo usada')  
            else:
                print(f'Falta una puerta y/o un monstruo ligado')  
        else:
            print(f'El monstruo no es asistente') 
    
    def asustar(self, pue):
        if(not self.__estadoDormido):
            if(pue and type(pue) == Puerta):
                if(pue.obtenerEstadoEnUso()):
                    if(pue.obtenerHumano() and pue.obtenerMonstruo() == self):
                        if(self.__tipo == 'asustador'):
                            if(not pue.obtenerHumano().obtenerEstadoAsustado()):
                                if(self.__energia - 10 >= self.min_Energia):
                                    self.__energia -= 10
                                    pue.obtenerHumano().establecerEstadoAsustado(True)
                                else:
                                    print(f'El monstruo no puede asustar porque no tiene energía')  
                            else:
                                print(f'El monstruo no puede asustar a un humano ya asustado')  
                        else:
                            print(f'El Monstruo no es un asustador')  
                    else:
                        print(f'La Puerta no tiene asignado a un Humano o esta siendo usada por otro monstruo')  
                else:
                    print(f'La Puerta no esta activa')  
            else:
                print(f'Se intento usar algo distinto a una Puerta')  
        else:
            print(f'El monstruo esta dormido') 
    
    def divertir(self, pue):
        if(not self.__estadoDormido):
            if(pue and type(pue) == Puerta):
                if(pue.obtenerEstadoEnUso()):
                    if(pue.obtenerHumano() and pue.obtenerMonstruo() == self):
                        if(self.__energia - 10 >= self.min_Energia):
                            self.__energia -= 10
                            pue.obtenerHumano().establecerEstadoAsustado(False)
                        else:
                            print(f'El monstruo no puede divertir porque no tiene energía')
                    else:
                        print(f'La Puerta no tiene asignado a un Humano o esta siendo usada por otro monstruo')  
                else:
                    print(f'La Puerta no esta activa')  
            else:
                print(f'Se intento usar algo distinto a una Puerta')  
        else:
            print(f'El monstruo esta dormido') 
    
    def dormir(self):
        if(self.__energia < self.max_energia):
            self.establecerEnergia(self.__energia + 15)
        else:
            print(f'El monstruo ya tiene la energia completa') 

    def despertar(self):
        if(not self.__estadoDormido):
            self.__estadoDormido = True
        else:
            print(f'El monstruo ya estaba despierto') 
    
    #consultas
    def obtenerNombre(self):
        return self.__nombre

    def obtenerEspecie(self):
        return self.__especie

    def obtenerEnergia(self):
        return self.__energia

    def obtenerTipo(self):
        return self.__tipo

    def obtenerPareja(self):
        return self.__pareja

    def __str__(self):
        return '[El monstruo ' + str(self.__nombre) + ', de especie ' + str(self.__especie) + ', tiene ' + str(self.__energia) + ' de energia]'