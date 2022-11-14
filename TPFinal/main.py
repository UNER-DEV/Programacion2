# Flask
from flask import Flask
from flask_restful import Api
import os

from biblioteca import Biblioteca

# API
from recursos import *

if __name__ == "__main__":
    Biblioteca.inicializar()

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(RecursoArtista, '/api/artistas/<id>')
    api.add_resource(RecursoArtistas, '/api/artistas')
    api.add_resource(RecursoAlbum, '/api/albumes/<id>')
    api.add_resource(RecursoAlbumes, '/api/albumes')
    api.add_resource(RecursoCancion, '/api/canciones/<id>')
    api.add_resource(RecursoCanciones, '/api/canciones')

    app.run(debug=True)
