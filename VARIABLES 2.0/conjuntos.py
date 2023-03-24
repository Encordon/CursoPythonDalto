#creando un conjunto con set

conjunto = set(["gato1","gato2"])

#introduciendo conjunto dentro otro conjunto
conjunto1 = frozenset(["gato1","gato2"])
conjunto2 = {conjunto1,"gato3"}

print(conjunto1)

#teoria de conjunto

conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

#verificando si es subconjunto
resultado = conjunto4.issubset(conjunto3) 
resultado = conjunto4 <= conjunto3

#verificando si es superconjunto
resultado2 = conjunto4.issuperset(conjunto3) #verificando si es superconjunto
resultado2 = conjunto4 >= conjunto3

#verificando si hay algun numero en comun
resultado3 = conjunto4.isdisjoint(conjunto3) #si coincide un numero arroja false



print(resultado)
print(resultado2)
print(resultado3)