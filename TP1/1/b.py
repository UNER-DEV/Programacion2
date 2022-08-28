# Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y 
# cuando las letras que componen dicha palabra estén en orden alfabético, y False en caso contrario.

def es_abc(palabra):   
    letras_ordenadas = "".join(sorted(palabra))
    if letras_ordenadas == palabra:
        #La palabra está ordenada
        return True
    return False


#es_abc("amor")  