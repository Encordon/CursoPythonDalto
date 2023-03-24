lista = list(["gato","perro","casa", 35]) #crea una lista con list


cantidad_elemento =len(lista) #devuelve cantidad de elementos en la lista

lista.append("Auto") #agrega elemento a la lista
lista.insert(2,"Deudas") #agrega elemento en un indice especifico
lista.extend(["lavadora","cocina"]) #agregando una lista en otra lista


lista.pop(3) #Elimina elemento en un indice especifico (con -1 elimina el ultimo, -2 el penultimo y sucesivamente)
lista.remove(35) #elimina un elemento de la lista por su valor
#lista.clear() elimina toda la lista


lista.sort (reverse=True) #ordena los elementos de la lista de forma ascendente con reverse lo contrario
lista.reverse() #invirtiendo el orden de la lista

elemento_encontrado = lista.index("perro") #verifica si un elemento se encuentra en una lista y muestra su indice

print (cantidad_elemento)
print (lista)
print (elemento_encontrado)



