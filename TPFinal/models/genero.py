import json


class Genero:

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre()
        }
