import json

class Integrante:

    # método de inicialización
    def __init__(self, nombre, instrumentos):
        self.__nombre = nombre
        self.__instrumentos = instrumentos

    # comandos
    def establecerNombre(self, nombre):
        self.__nombre = nombre

    def establecerInstrumentos(self, instrumentos):
        self.__instrumentos = instrumentos

    #consultas
    def obtenerNombre(self):
        return self.__nombre

    def obtenerInstrumentos(self):
        return self.__instrumentos

    def __eq__(self, other):
        return self.__nombre == other.obtenerNombre()

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre(),
            "instrumentos": self.obtenerInstrumentos()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "instrumentos": self.obtenerInstrumentos()
        }
