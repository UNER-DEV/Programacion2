class Monstruo():
    max_energia = 100

    # método de inicialización
    def __init__(self,nombre,esp):
        self.__nombre = nombre
        self.__especie = esp
        self.__energia = self.max_energia

    # comandos
    def establecerNombre(self,nombre):
        self.__nombre = nombre
    def establecerEspecie(self, esp):
        self.__especie = esp
    def establecerEnergia(self, energia):
        self.__energia = energia

    #Se modificó el comando asustar y se añadió divertir
    def asustar(self, hum):
        if(self.__energia-10>0):
            self.__energia-=10
            hum.establecerEstadoAsustado(True)
        else:
            print(f'El monstruo no puede asustar porque no tiene energía')  
    def divertir(self, hum):
        if(self.__energia-20>0):
            self.__energia-=20
            hum.establecerEstadoAsustado(False)
        else:
            print(f'El monstruo no puede divertir porque no tiene energía')

    #consultas
    def obtenerNombre(self):
        return self.__nombre
    def obtenerEspecie(self):
        return self.__especie
    def obtenerEnergia(self):
        return self.__energia
    def __str__(self):
        return '[El monstruo '+str(self.__nombre)+', de especie '+str(self.__especie)+', tiene '+str(self.__energia)+' de energia]'
    

