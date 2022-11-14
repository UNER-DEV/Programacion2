import json

import biblioteca

class Album:

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "anio": self.obtenerAnio(),
            "artista": self.obtenerArtista().obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "anio": self.obtenerAnio()
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "anio": self.obtenerAnio(),
            "artista": self.obtenerArtista().obtenerNombre(),
            "canciones": self._mapearCanciones()
        }

    def _mapearCanciones(self):
        canciones = self.obtenerCanciones()
        cancionesMapa = map(lambda c: c.obtenerNombre(), canciones)
        return list(cancionesMapa)
