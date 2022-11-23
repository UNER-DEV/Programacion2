import json
import biblioteca
class Album:

    # método de inicialización
    def __init__(self, id, nombre, anio, genero, artista, canciones):
        self.__id = id
        self.__artista = artista
        self.__nombre = nombre
        self.__anio = anio
        self.__genero = genero
        self.__canciones = canciones

    # comandos
    def establecerNombre(self, nombre):
        self.__nombre = nombre
        
    def establecerAnio(self, anio):
        self.__anio = anio

    def establecerGenero(self, genero):
        self.__genero = genero

    def establecerArtista(self, artista):
        self.__artista = artista
        
    #consultas
    def obtenerId(self):
        return self.__id
        
    def obtenerNombre(self):
        return self.__nombre

    def obtenerAnio(self):
        return self.__anio

    def obtenerGenero(self):
        return biblioteca.Biblioteca.buscarGenero(self.__genero)

    def obtenerArtista(self):
        return biblioteca.Biblioteca.buscarArtista(self.__artista)

    def obtenerCanciones(self):
        cancionesList= []
        for cancion in self.__canciones:
            cancionesList.append(biblioteca.Biblioteca.buscarCancion(cancion["id"]))
        return cancionesList

    def __eq__(self, other):
        return self.__id == other.obtenerId()
        
    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "anio": self.obtenerAnio(),
            "artista": self.obtenerArtista().obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "anio": self.obtenerAnio()
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "anio": self.obtenerAnio(),
            "artista": self.obtenerArtista().obtenerNombre(),
            "canciones": self._mapearCanciones()
        }

    def _mapearCanciones(self):
        canciones = self.obtenerCanciones()
        cancionesMapa = map(lambda c: c.obtenerNombre(), canciones)
        return list(cancionesMapa)
