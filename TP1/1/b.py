# Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y 
# cuando las letras que componen dicha palabra estén en orden alfabético, y False en caso contrario.
from modules.utils import *
clear()

def es_abc(palabra):   
    letras_ordenadas = "".join(sorted(palabra))
    if letras_ordenadas == palabra:
        print("El programa retorna True")
        return True
    print("El programa retorna False")
    return False


#Test: 
#es_abc("amor")  