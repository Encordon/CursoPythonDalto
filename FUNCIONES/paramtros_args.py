#forma no optima de sumar valores
def suma(lista):
    numero_sumados = 0
    for numero in lista:
        numero_sumados = numero_sumados + numero
    return numero_sumados

resultado = suma([3,4,5,6,7]) 
print(resultado)
print("-------")

#optimizando con args
def suma(nombre,*numeros):
    return f'{nombre}, la suma de tu numeros es : {sum(numeros)}' #sum es funcion que suma valores de la lista

resultado1 = suma('Enrique',3,4,5,6,7)
print (resultado1)
print ('------')

#otra manera de sumar valores la mas optima
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([3,4,5,6,7])
print(resultado2)