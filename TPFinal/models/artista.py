import json

import biblioteca


class Artista:

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "albumes": self._mapearAlbumes(),
            "canciones": len(self.obtenerCanciones())
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "albumes": self._mapearAlbumes(),
            "canciones": self._mapearCanciones()
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
