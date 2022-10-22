from Humano import *
from Monstruo import *
from Puerta import *
from MonstersInc import *

class TesterMonstersInc:

    def main(self):
        #Se utilizan las ultimas versiones de las clases
        #Se crean los objetos de prueba
        monsterInc = MonstersInc();
        sulivan = Monstruo('James P. Sullivan', 'leon', 'asustador');
        mike = Monstruo('Mike Wazowski', 'ciclope', 'asistente');
        boo = Humano('Boo');
        puerta = Puerta(1, boo);
        #5.a-->
        parejaMonstruo = {"asustador": mike, "asistente": sulivan}
        monsterInc.agregarMonstruos(parejaMonstruo);
        monsterInc.agregarPuerta(puerta);
        monsterInc.eliminarPuerta(puerta);
        monsterInc.eliminarMonstruos(parejaMonstruo);
        #5.a-->
        monsterInc.agregarMonstruos(parejaMonstruo);
        monsterInc.agregarPuerta(puerta);
        mike.establecerPareja(sulivan);
        mike.activarPuerta(puerta, mike.obtenerPareja());
        #5.b-->
        sulivan.asustar(puerta);
        #5.b-->

        #5.c-->
        sulivan.divertir(puerta);
        #5.c-->

        sulivan.asustar(puerta);

        #5.d-->
        sulivan.asustar(puerta);                #5.d-i
        sulivan.establecerEnergia(20);
        sulivan.divertir(puerta);               #5.d-ii
        puerta.establecerEstadoActiva(False);
        sulivan.divertir(puerta);               #5.d-iii
        puerta.establecerEstadoActiva(True);
        mike.divertir(puerta);                  #5.d-iv
        #5.d-->

        #5.c-->
        print(f'Energia antes de dormir = {sulivan.obtenerEnergia()}');
        sulivan.dormir();
        print(f'Energia despues de dormir = {sulivan.obtenerEnergia()}');
        #5.c-->
if __name__ == '__main__':
        test = TesterMonstersInc();
        test.main();