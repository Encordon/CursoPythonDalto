#creado funcion de 3 parametros
def frase (nombre,apellido,edad):
    return f'hola {nombre} {apellido}, tienes {edad} años'
frase_resultante = frase ("Enrique", 'Cordon', 29)
print(frase_resultante)
print ('------')

#utilizando keywords
def frase1 (nombre,apellido,edad):
    return f'hola {nombre} {apellido}, tienes {edad} años'
frase_resultante1 = frase (apellido ='Cordon',edad = 29, nombre ="Enrique")
print(frase_resultante1)