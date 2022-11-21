# Flask
from flask import Flask, render_template,request
from flask_restful import Api
import os
from biblioteca import Biblioteca
# API
from recursos import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout_base.html') #Flask busca, por defecto la ruta de las plantillas.

@app.get("/api/artistas")
def getArtistas():
    data = []
    try:
        data = recursos.RecursoArtista.get
    except:
        print("JSON Vacio")
    return render_template('artistas.html',data=data, len = len(data))

@app.get("/api/albumes")
def getAlbums():
    return render_template('albums.html')

@app.get("/api/canciones")
def getCanciones():
    return render_template('canciones.html')


if __name__ == '__main__':
    Biblioteca.inicializar()
    #Routes
    api = Api(app)
    api.add_resource(RecursoArtista, '/api/artistas/<id>')
    api.add_resource(RecursoArtistas, '/api/artistas')
    api.add_resource(RecursoAlbum, '/api/albumes/<id>')
    api.add_resource(RecursoAlbumes, '/api/albumes')
    api.add_resource(RecursoCancion, '/api/canciones/<id>')
    api.add_resource(RecursoCanciones, '/api/canciones')
    app.run(debug=True)
    #app.run()