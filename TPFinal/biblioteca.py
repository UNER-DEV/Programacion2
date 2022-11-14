# librerias
import os
import json

# modelos
from models.artista import Artista
from models.banda import Banda
from models.cancion import Cancion
from models.album import Album
from models.genero import Genero


class Biblioteca:

    __archivoDeDatos = "biblioteca.json"
    __artistas = []
    __canciones = []
    __albumes = []
    __generos = []

    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)

    def obtenerArtistas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'tipo':
                pass
        pass

    def obtenerCanciones(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'artista':
                pass
        pass

    def obtenerAlbumes(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'artista':
                pass
            elif orden == 'anio':
                pass
        pass

    def obtenerGeneros(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
        pass
    
    def buscarArtista(id):
        pass

    def buscarCancion(id):
        pass
    
    def buscarAlbum(id):
        pass

    def buscarGenero(id):
        pass
    
    def __parsearArchivoDeDatos():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "db", Biblioteca.__archivoDeDatos)
        dataLocal = json.load(open(json_url))
        return dataLocal;

    def __convertirJsonAListas(lista):
        pass
