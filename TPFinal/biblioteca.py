# librerias
import os
import json

# modelos
from models.artista import Artista
from models.banda import Banda
from models.cancion import Cancion
from models.album import Album
from models.genero import Genero
from models.integrante import Integrante

class Biblioteca:

    __archivoDeDatos = "biblioteca.json"
    artistas = []
    canciones = []
    albumes = []
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
        # if isinstance(orden, str):
        #     if orden == 'nombre':
        #         pass
        #     elif orden == 'artista':
        #         pass
        return Biblioteca.canciones

    def obtenerAlbumes(orden=None, reverso=False):
        # if isinstance(orden, str):
        #     if orden == 'nombre':
        #         pass
        #     elif orden == 'artista':
        #         pass
        #     elif orden == 'anio':
        #         pass
        return Biblioteca.albumes

    def obtenerGeneros(orden=None, reverso=False):
        # if isinstance(orden, str):
        #     if orden == 'nombre':
        #         pass
        return Biblioteca.generos
    
    def buscarArtista(id):
        for artist in Biblioteca.artistas:
            artistId = artist.obtenerId()
            if(artistId == id):
                return artist
        return None


    def buscarCancion(id):
        for cancion in Biblioteca.canciones:
            cancionId = cancion.obtenerId()
            if(cancionId == id):
                return cancion
        return None
    
    def buscarAlbum(id):
        for album in Biblioteca.albumes:
            albumId = album.obtenerId()
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
        #Generos
        for genero in lista["generos"]:
            genre = Genero(genero["id"],genero["nombre"])
            if(genre not in Biblioteca.generos):
                Biblioteca.generos.append(genre)
        #Artistas
        for artista in lista["artistas"]:
            if(artista["tipo"] == "solista"):
                artist = Artista(artista["id"], artista["nombre"], artista["tipo"], Biblioteca.buscarGenero(artista["genero"]), None, None)
            else:
                integrantes = []
                for integrante in artista["integrantes"]:
                    integrantes.append(Integrante(integrante["nombre"], integrante["instrumentos"]))
                artist = Banda(artista["id"], artista["nombre"], artista["tipo"], Biblioteca.buscarGenero(artista["genero"]), integrantes, None, None)
            if(artist not in Biblioteca.artistas):
                Biblioteca.artistas.append(artist)
        #Canciones
        for cancion in lista["canciones"]:
            song = Cancion(cancion["id"], cancion["nombre"], Biblioteca.buscarArtista(cancion["artista"]),None)
            if(song not in Biblioteca.canciones):
                Biblioteca.canciones.append(song)
        #Albumes
        for album in lista["albumes"]:
            cancionesAlbum = []
            for cancion in album["canciones"]:
                Biblioteca.buscarCancion(cancion["id"]).establecerOrden(str(cancion["orden"]))
                cancionesAlbum.append(Biblioteca.buscarCancion(cancion["id"]))
            alb = Album(album["id"], Biblioteca.buscarArtista(album["artista"]), album["nombre"], album["anio"], Biblioteca.buscarGenero(album["genero"]), cancionesAlbum)
            if(alb not in Biblioteca.albumes):
                Biblioteca.albumes.append(alb)
