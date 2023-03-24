
numeros = [1,2,3,4,5,6,7,8,9]

#creando una funcion lamda para multiplicar x2
duplicar = lambda x : x*2

#creando funcion comun que diga si es par
def es_par(num):
    if (num%2==0):
        return True


#usando filter con una funcion comun
numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))
print('------')

#creando misma funcion anterior con lambda
numeros_pares_lambda = filter(lambda numero:numero%2 == 0, numeros)

print(list(numeros_pares_lambda))


