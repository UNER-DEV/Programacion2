import json

import biblioteca


class Cancion:

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "artista": self.obtenerArtista().obtenerNombre(),
            "album": self.obtenerAlbum().obtenerNombre()
        }
        
    def convertirAJSONFull(self):
        return self.convertirAJSON()
