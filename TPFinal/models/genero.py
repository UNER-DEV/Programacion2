import json

class Genero:

    # método de inicialización
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    # comandos
    def establecerId(self, id):
        self.__id = id

    def establecerNombre(self, nombre):
        self.__nombre = nombre

    #consultas
    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def __eq__(self, other):
        return self.__id == other.obtenerId()

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre()
        }
