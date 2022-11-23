import json

import biblioteca

class Artista:

    # método de inicialización
    def __init__(self, id, nombre, tipo, genero):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__genero = genero

    # comandos

    def establecerNombre(self, nombre):
        self.__nombre = nombre
    def establecerTipo(self, tipo):
        self.__tipo = tipo
    def establecerGenero(self, genero):
        self.__genero = genero

    #consultas
    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def obtenerTipo(self):
        return self.__tipo

    def obtenerGenero(self):
        return biblioteca.Biblioteca.buscarGenero(self.__genero)

    def obtenerAlbumes(self):
        albumList= []
        for album in biblioteca.Biblioteca.obtenerAlbumes():
            if(self == album.obtenerArtista()):
                albumList.append(album)
        return albumList

    def obtenerCanciones(self):
        cancionesList= []
        for cancion in biblioteca.Biblioteca.obtenerCanciones():
            if(self == cancion.obtenerArtista()):
                cancionesList.append(cancion)
        return cancionesList

    def __str__(self):
        return '[El '+ str(self.__tipo) + ' ' + str(self.__nombre) +', de genero ' + str(self.__genero) + ']'

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def __eq__(self, other):
        return self.__id == other.obtenerId()

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre()
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre()
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
