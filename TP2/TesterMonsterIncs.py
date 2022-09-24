from MonstersInc import *
from modules.utils import *

class TesterMonstersInc:
    def main(self):
        empresa = MonsterInc()
        while True:
            clear()
            list = ['Agregar Humano','Agregar Monstruo','Filtrar montruos segun energia','Filtrar humanos segun estado','Salir']
            value = crearOpciones(list)
            clear()
            crearCartel(list[int(value)-1])
            if value == str(len(list)):
                break
            if value == '1':
                name = normalizar(str(input('\nIngrese el nombre del Humano a agregar>> ')))
                empresa.agregarHumano(Humano(name))
            if value == '2':
                print('Monstruos + 1')
            if value == '3':
                print('Mostrar Mon')
            if value == '4':
                print('Mostrar Hum')

# Solución de los puntos 6.a., 6.b, 6.c, ...
if __name__ == '__main__':
    testerMonstersInc = TesterMonstersInc()
    testerMonstersInc.main()