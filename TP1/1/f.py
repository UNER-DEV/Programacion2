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

import re
#{6-20}

def contrasena_valida(contrasena):
    val=re.compile('.[A-Z]{2,}?')
    if val.match(contrasena):
        print("vamoloco")
    else:
        print("noentro wey")

#Test:
contrasena_valida("AbC")