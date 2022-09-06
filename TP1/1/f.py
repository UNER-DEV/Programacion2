# Un portal web requiere un formulario de alta de usuario donde se ingrese, mínimamente, un usuario y su correspondiente contraseña. 
# Escriba, en Python, una función contrasena_valida(contrasena) que devuelva True en caso de superar las siguientes validaciones 
# sobre la contraseña proporcionada por el usuario:
# i. Longitud entre 6 y 20 caracteres.
# ii. Debe contener al menos un número.
# iii. Debe contener al menos dos mayúsculas.
# iv. Debe contener al menos un carácter especial.
# v. No puede contener espacios.

# La salida esperada es la siguiente:
# abc.123 es válida: False
# Abc.123 es válida: False
# AbC.123 es válida: True
# AbC.1 23 es válida: False
# ÁbC.123 es válida: False

from modules.utils import *
import re



def contrasena_valida(entrada):
    if(len(entrada)>=6 and len(entrada)<= 20):
        respuesta = True
        # Tiene numeros?
        if len(re.findall(r'\d',entrada)) == 0:
            respuesta = False
        # Tiene caracteres especiales?
        if len(re.findall("[$&+,:;=?@#|<>.^*()%!-]",entrada)) == 0:
            respuesta = False
        # tiene dos o mas mayusculas?
        if len(re.findall(r'[A-Z]',entrada)) < 2:
            respuesta = False
        # espacios en blanco
        if len(re.findall(r'\s',entrada)) > 0:
            respuesta = False
        # No puede tener tilde
        #if len(re.findall(r'[A-Za-z0-9]',entrada))+len(re.findall("[$&+,:;=?@#|<>.^*()%!-]",entrada)) != len(entrada):
        if len(re.findall("[ÁáÉéÍíÓóÚú]",entrada))>0:
            respuesta = False
    else:
        respuesta = False

    return respuesta
    


#Test:
print(contrasena_valida("abc.123"))
print(contrasena_valida("Abc.123"))
print(contrasena_valida("AbC.123"))
print(contrasena_valida("AbC.1 23"))
print(contrasena_valida("ÁBC.123"))
print(contrasena_valida(""))
print(contrasena_valida("AbC.AbC"))
print(contrasena_valida("AbCqAbC"))
print(contrasena_valida("AbC.123AbC.123AbC.123AbC.123AbC.123"))
