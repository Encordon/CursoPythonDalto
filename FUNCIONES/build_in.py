numeros = [5,7,8,4,6,20]

#encontrando el numero mayor de la lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)
print("------")


#encontrando el numero menor de la lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)
print("------")


#redondeando a N decimales
numero = round(12.5363636,2) #funcion round (numero, cantidad de decimales)
print(numero)
print("------")


#retorna false -> 0, vacio, false, ninguno, true ,cadena,datos
resultado_bool = bool()
print(resultado_bool)
print('-----')
resultado_bool1 = bool((2,4))
print(resultado_bool1)

#retorna true, si todos los valores son verdaderos
resultado_all = all([1,"gato",[2,4]])
print(resultado_all)


#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)