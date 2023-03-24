#creando diccionario con dict()
diccionario = dict(nombre="Enrique", apellido="Cordon")
                   
#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["cordon", "gato"]): "pan"}    

#creando diccionarios con fromkeys() valor por defecto none
diccionario = dict.fromkeys(["nombre","apellidos"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a Gatitos
diccionario = dict.fromkeys(["nombre","apellidos"],"gatitos")



print(diccionario)              