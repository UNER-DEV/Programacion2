import json
from biblioteca import Biblioteca

class Cancion:
    
    # método de inicialización
    def __init__(self, id, nombre, artista,orden,album):
        self.__id = id
        self.__nombre = nombre
        self.__artista = artista
        self.__orden = orden
        self.__album = album

    # comandos
    def establecerId(self, id):
        self.__id = id
        
    def establecerNombre(self, nombre):
        self.__nombre = nombre
        
    def establecerArtista(self, artista):
        self.__artista = artista
    def establecerOrden(self, orden):
        self.__orden = orden
    def establecerAlbum(self, album):
        self.__album = album
    #consultas
    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre
        
    def obtenerArtista(self):
        return Biblioteca.buscarArtista(self.__artista)
    def obtenerOrden(self):
        return self.__orden
    def obtenerAlbum(self):
        return self.__album

    def __eq__(self, other):
        return self.__id == other.obtenerId()

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "artista": self.obtenerArtista().obtenerNombre(),
            "album": self.obtenerAlbum().obtenerNombre()
        }
        
    def convertirAJSONFull(self):
        return self.convertirAJSON()
