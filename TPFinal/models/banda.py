import json
from models.artista import Artista
import biblioteca
class Banda(Artista):

    # método de inicialización
    def __init__(self, id, nombre, tipo, genero, integrantes):
        super().__init__(id, nombre, tipo, genero)
        self.__integrantes = integrantes

    def establecerIntegrantes(self, integrantes):
        self.__integrantes = integrantes

    #consultas
    def obtenerIntegrantes(self):
        return self.__integrantes

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "integrantes": self.obtenerIntegrantes()
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "integrantes": self.obtenerIntegrantes()
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
