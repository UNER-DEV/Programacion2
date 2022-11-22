# librerias
import os
import json

# modelos
from models.artista import Artista
#from models.banda import Banda
from models.cancion import Cancion
from models.album import Album
from models.genero import Genero


class Biblioteca:

    __archivoDeDatos = "biblioteca.json"
    artistas = []
    __canciones = []
    __albumes = []
    generos = []
    datos = []

    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)

    def obtenerArtistas(orden=None, reverso=False):
        # if isinstance(orden, str):
        #     if orden == 'nombre':
        #         Biblioteca.artistas = sorted(Biblioteca.artistas, key=itemgetter('nombre'),reverse=reverso )
        #     elif orden == 'tipo':
        #         Biblioteca.artistas = sorted(Biblioteca.artistas, key=itemgetter('tipo'),reverse=reverso )
        return Biblioteca.artistas

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
        artists = datos["artistas"]
        for artist in artists:
            artistId = artist["id"]
            if(artistId == id):
                return artist
            else:
                return None


    def buscarCancion(id):
        songs = datos["canciones"]
        for song in songs:
            songId = song["id"]
            if(songId == id):
                return song
            else:
                return None
    
    def buscarAlbum(id):
        albums = datos["albumes"]
        for album in albums:
            albumId = album["id"]
            if(albumId == id):
                return album
        return None


    def buscarGenero(id):
        for genero in Biblioteca.generos:
            genderId = genero.obtenerId()
            if(genderId == id):
                return genero
        return None


    #obtengo un diccionario con datos del json
    def __parsearArchivoDeDatos():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "db", Biblioteca.__archivoDeDatos)
        dataLocal = json.load(open(json_url))
        return dataLocal

    def __convertirJsonAListas(lista):
        for genero in lista["generos"]:
            genre = Genero(genero["id"],genero["nombre"])
            if(genre not in Biblioteca.generos):
                Biblioteca.generos.append(genre)
        for artista in lista["artistas"]:
            artist = Artista(artista["id"],artista["nombre"],artista["tipo"],Biblioteca.buscarGenero(artista["genero"]),None,None)
            if(artist not in Biblioteca.artistas):
                Biblioteca.artistas.append(artist)

