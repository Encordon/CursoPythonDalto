animales = ["perro","gato","loro","conejo","tortuga"]
numeros = [10,20,30,40,50]

#recorriendo la lista animales
for animal in animales :
    print(f'Ahora la varible animal es igual a {animal}')
    print ("            ")
    
    
#recorriendo la lista numeros y multiplicando por 10
for numero in numeros :
    resultado = numero *10
    print(resultado)
    
#iterando dos listas del mismo tamño al mismo tiempo zip()   
for numero, animal in zip(animales,numeros) :
    print(f"recorriendo lista 1: {numero}")
    print(f'recorriendo lsta 2:{animal}')
    
    
for num in range(3,10) :
    print(num)
    print("---------")
    
#forma no optima de recorrer una lista y tupla (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    print("-------")
    
#forma correcta recorrer una lista con su indice
for num in enumerate(numeros) :
    indice = num[0]
    valor = num [1]
    print(f'el indice es {indice} y el valor es {valor}')
    print('-------')
    
    
#usando el else en for
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual:{numero}')
else :
    print("El bucle termino")
    
    
#todo lo anterior se aplica a tuplas y conjuntos