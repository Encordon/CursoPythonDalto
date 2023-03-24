diccionario = {
    "nombre" : 'perro',
    "apellido" : 'gato',
    "años" : 35
}

claves = diccionario.get ("nombre") #obteniendo un elemento con get() si no encuentra nada el programa continua
elementos = diccionario.keys()
#diccionario.clear() elimina todo el diccionario

diccionario.pop ("apellido") #elimina elementos del diccionario

diccionario_iterable = diccionario.items()

print(claves)
print(elementos)
print(diccionario_iterable)