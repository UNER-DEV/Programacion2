import json
import biblioteca
class Cancion:
    
    # método de inicialización
    def __init__(self, id, nombre, artista):
        self.__id = id
        self.__nombre = nombre
        self.__artista = artista

    # comandos
    def establecerNombre(self, nombre):
        self.__nombre = nombre
        
    def establecerArtista(self, artista):
        self.__artista = artista

    #consultas
    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre
        
    def obtenerArtista(self):
        return biblioteca.Biblioteca.buscarArtista(self.__artista)

    def obtenerAlbum(self):
        for album in biblioteca.Biblioteca.obtenerAlbumes():
            for cancion in album.obtenerCanciones():
                if(self.__id == cancion.obtenerId()):
                    return album
        return None

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
