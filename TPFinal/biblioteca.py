# librerias
import os
import json

import models.genero


# modelos
from models.artista import Artista
from models.banda import Banda
from models.cancion import Cancion
from models.album import Album
from models.genero import Genero
from models.integrante import Integrante

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
                Biblioteca.__artistas = sorted(Biblioteca.__artistas, key=itemgetter('nombre'),reverse=reverso )
            elif orden == 'tipo':
                Biblioteca.__artistas = sorted(Biblioteca.__artistas, key=itemgetter('tipo'),reverse=reverso )
        return Biblioteca.__artistas

    def obtenerCanciones(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'artista':
                pass
        return Biblioteca.__canciones

    def obtenerAlbumes(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'artista':
                pass
            elif orden == 'anio':
                pass
        return Biblioteca.__albumes

    def obtenerGeneros(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
        return Biblioteca.__generos
    
    def buscarArtista(id):
        for artist in Biblioteca.__artistas:
            artistId = artist.obtenerId()
            if(artistId == id):
                return artist
        return None


    def buscarCancion(id):
        for cancion in Biblioteca.__canciones:
            cancionId = cancion.obtenerId()
            if(cancionId == id):
                return cancion
        return None
    
    def buscarAlbum(id):
        for album in Biblioteca.__albumes:
            albumId = album.obtenerId()
            if(albumId == id):
                return album
        return None

    def buscarGenero(id):
        for genero in Biblioteca.__generos:
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
        #Generos
        for genero in lista["generos"]:
            genre = Genero(genero["id"],genero["nombre"])
            if(genre not in Biblioteca.__generos):
                Biblioteca.__generos.append(genre)
        #Artistas
        for artista in lista["artistas"]:
            if(artista["tipo"] == "solista"):
                artist = Artista(artista["id"], artista["nombre"], artista["tipo"], artista["genero"])
            else:
                integrantes = []
                for integrante in artista["integrantes"]:
                    integrantes.append(Integrante(integrante["nombre"], integrante["instrumentos"]))
                artist = Banda(artista["id"], artista["nombre"], artista["tipo"], artista["genero"], integrantes)
            if(artist not in Biblioteca.__artistas):
                Biblioteca.__artistas.append(artist)
        #Canciones
        for cancion in lista["canciones"]:
            song = Cancion(cancion["id"], cancion["nombre"], cancion["artista"])
            if(song not in Biblioteca.__canciones):
                Biblioteca.__canciones.append(song)
        #Albumes
        for album in lista["albumes"]:
            alb = Album(album["id"], album["nombre"], album["anio"], album["genero"], album["artista"], album["canciones"])

            if(alb not in Biblioteca.__albumes):
                Biblioteca.__albumes.append(alb)

