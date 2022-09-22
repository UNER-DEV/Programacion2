
class Humano():
    especie = "Humano"

    # método de inicialización
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__estadoAsustado = False
    
     # comandos
    def establecerNombre(self,nombre):
        self.__nombre = nombre
    def establecerEstadoAsustado(self,estado):
        self.__estadoAsustado = estado

    #consultas
    def obtenerNombre(self):
        return self.__nombre
    def obtenerEstadoAsustado(self):
        return self.__estadoAsustado
    def __str__(self):
        return '['+str(self.__nombre)+','+str(self.__estadoAsustado)+']'
