import json

class Banda:

    # método de inicialización
    def __init__(self, id, nombre, tipo, genero, integrantes, albumes, canciones):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__genero = genero
        self.__integrantes = integrantes
        self.__albumes = albumes
        self.__canciones = canciones

    # comandos
    def establecerId(self, id):
        self.__id = id

    def establecerNombre(self, nombre):
        self.__nombre = nombre

    def establecerTipo(self, tipo):
        self.__tipo = tipo

    def establecerGenero(self, genero):
        self.__genero = genero

    def establecerIntegrantes(self, integrantes):
        self.__integrantes = integrantes

    def establecerAlbumes(self, albumes):
        self.__albumes = albumes

    def establecerCanciones(self, canciones):
        self.__canciones = canciones

    #consultas
    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def obtenerTipo(self):
        return self.__tipo

    def obtenerGenero(self):
        return self.__genero

    def obtenerIntegrantes(self):
        return self.__integrantes

    def obtenerAlbumes(self):
        return self.__albumes

    def obtenerCanciones(self):
        return self.__canciones

    def __str__(self):
        return '[La '+ str(self.__tipo) + ' ' + str(self.__nombre) +', de genero ' + str(self.__genero) + ']'

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def __eq__(self, other):
        return self.__id == other.obtenerId()

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "integrantes": self.obtenerGenero().obtenerIntegrantes(),
            "albumes": None, #self._mapearAlbumes(),
            "canciones": 0 #len(self.obtenerCanciones())
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "integrantes": self.obtenerGenero().obtenerIntegrantes(),
            "albumes": None, #self._mapearAlbumes(),
            "canciones": None #self._mapearCanciones()
        }

    def _mapearAlbumes(self):
        albumes = self.obtenerAlbumes()
        albumesMapa = map(
            lambda a: {"nombre": a.obtenerNombre(), "anio": a.obtenerAnio()}, albumes)
        return list(albumesMapa)

    def _mapearCanciones(self):
        canciones = self.obtenerCanciones()
        cancionesMapa = map(lambda c: c.obtenerNombre(), canciones)
        return list(cancionesMapa)
