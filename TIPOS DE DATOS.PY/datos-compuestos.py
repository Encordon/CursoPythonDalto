lista = ["Enrique","computadora",True,1.2]
#en lista los datos son modificables

tupla = ("Enrique","computadora",True,1.2)
#tupla los datos no se pueden modificar

lista [3] = 1.5
#se ha modificado el 1.2 por 1.5


#creando un conjunto (set)

conjunto = {"Enrique","computadora",True,1.2,"computadora"}
#conjunto no almacena datos duplicados, no accede a elementos por indice



#creando un diccionario (dict)/ 'key' : 'value'y separamos con coma
diccionario = {
    'nombre' : 'Enrique',
    'pais' :  'Nicaragua',
    'altura' : 1.74,
    'dato_constante' : 'Nicaragua'    
}


print (lista [3])
print (tupla[3])
print (conjunto)
print (diccionario['altura'] + lista[3] + tupla[3])