from MonstersInc import *
from modules.utils import *
class TesterMonstersInc:
    def main(self):
        empresa = MonstersInc()
        while True:
            list = ['Agregar Humano','Agregar Monstruo','Filtrar montruos segun energia','Filtrar humanos segun estado','Salir']
            value = crearOpciones(list)
            crearCartel(list[int(value)-1])
            clear()
            if value == str(len(list)):
                break
            if value == '1':
                name = normalizar(str(input('\nIngrese el nombre del Humano a agregar>> ')))
                clear()
                empresa.agregarHumano(Humano(name))
            if value == '2':
                name = normalizar(str(input('\nIngrese el nombre del Monstruo a agregar>> ')))
                species = normalizar(str(input('\nIngrese la especie del Monstruo a agregar>> ')))
                clear()
                empresa.agregarMonstruo(Monstruo(name, species))
            if value == '3':
                value = int(checkNumero(str(input('\nIngrese el valor maximo de energia>> '))))
                clear()
                empresa.obtenerMonstruosByEnegia(value)
            if value == '4':
                clear()
                print(f'\nIngrese [si] para mostrar los asustados>> ')
                print(f'\nIngrese [no] para mostrar los calmados>> ')
                msg = checkInputSiNo('')
                clear()
                empresa.obtenerHumanosByEstado(msg == 'si')

# Solución de los puntos 6.a., 6.b, 6.c, ...
if __name__ == '__main__':
    testerMonstersInc = TesterMonstersInc()
    testerMonstersInc.main()