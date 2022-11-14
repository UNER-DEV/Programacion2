from flask_restful import Resource
from flask import request

import json

import biblioteca

from models.album import Album
from models.artista import Artista
from models.cancion import Cancion


class RecursoArtista(Resource):

    def get(self, id):
        artista = biblioteca.Biblioteca.buscarArtista(id)
        if isinstance(artista, Artista):
            return json.loads(json.dumps(artista.convertirAJSONFull())), 200
        else:
            return {"error": "Artista no encontrado"}, 404


class RecursoArtistas(Resource):

    def get(self):
        orden = request.args.get('orden')
        if (orden):
            reverso = request.args.get('reverso')
            artistas = biblioteca.Biblioteca.obtenerArtistas(
                orden=orden, reverso=reverso == 'si')
        else:
            artistas = biblioteca.Biblioteca.obtenerArtistas()
        return json.loads(json.dumps(artistas, default=lambda o: o.convertirAJSON())), 200


class RecursoAlbum(Resource):

    def get(self, id):
        album = biblioteca.Biblioteca.buscarAlbum(id)
        if isinstance(album, Album):
            return json.loads(json.dumps(album.convertirAJSONFull())), 200
        else:
            return {"error": "Album no encontrado"}, 404


class RecursoAlbumes(Resource):

    def get(self):
        orden = request.args.get('orden')
        if (orden):
            reverso = request.args.get('reverso')
            albumes = biblioteca.Biblioteca.obtenerAlbumes(
                orden=orden, reverso=reverso == 'si')
        else:
            albumes = biblioteca.Biblioteca.obtenerAlbumes()
        return json.loads(json.dumps(albumes, default=lambda o: o.convertirAJSONFull())), 200


class RecursoCancion(Resource):

    def get(self, id):
        cancion = biblioteca.Biblioteca.buscarCancion(id)
        if isinstance(cancion, Cancion):
            return json.loads(json.dumps(cancion.convertirAJSON())), 200
        else:
            return {"error": "Cancion no encontrada"}, 404


class RecursoCanciones(Resource):

    def get(self):
        orden = request.args.get('orden')
        if (orden):
            reverso = request.args.get('reverso')
            canciones = biblioteca.Biblioteca.obtenerCanciones(
                orden=orden, reverso=reverso == 'si')
        else:
            canciones = biblioteca.Biblioteca.obtenerCanciones()
        return json.loads(json.dumps(canciones, default=lambda o: o.convertirAJSON())), 200
