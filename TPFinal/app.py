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
    return render_template('home.html') #Flask busca, por defecto la ruta de las plantillas.

@app.get("/api/artistas")
def getArtistas():
    try:
        Biblioteca.inicializar()
        data = Biblioteca.obtenerArtistas()
    except:
        print("JSON Vacio")
    return render_template('artistas.html',data=data,len=len(data))

@app.get("/api/albumes")
def getAlbums():
    try:
        Biblioteca.inicializar()
        data = Biblioteca.obtenerAlbumes()
    except:
        print("JSON Vacio")
    return render_template('albums.html', data = data,len=len(data) )

@app.get("/api/canciones")
def getCanciones():
    try:
        Biblioteca.inicializar()
        data = Biblioteca.obtenerCanciones()
    except:
        print("JSON Vacio")
    return render_template('canciones.html', data = data, len=len(data))

@app.post("/api/canciones")
def searchCanciones():
    data= []
    id = request.form["id"]
    try:
        Biblioteca.inicializar()
        if(id!=None):
            data.append(Biblioteca.buscarCancion(id))
    except:
        print("JSON Vacio")
    return render_template('canciones.html', data = data, len=len(data))

@app.post("/api/albumes")
def searchAlbumes():
    data= []
    id = request.form["id"]
    try:
        Biblioteca.inicializar()
        if(id!=None):
            data.append(Biblioteca.buscarAlbum(id))
    except:
        print("JSON Vacio")
    return render_template('albums.html', data = data, len=len(data))

@app.post("/api/artistas")
def searchArtistas():
    data= []
    id = request.form["id"]
    try:
        Biblioteca.inicializar()
        data.append(Biblioteca.buscarArtista(id))
    except:
        print("JSON Vacio")
    return render_template('artistas.html', data = data, len=len(data))

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