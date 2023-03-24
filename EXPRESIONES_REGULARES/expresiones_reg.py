import re


texto = '''Hola pofy, esta es la linea1, como estas mi bro
esta es la linea2
y al parecer esta es la linea3'''

#Haciendo una busqueda simple
resultado1 = re.findall('Hola',texto)

#\d -> busca digitos numericos del 0 al 9 en mayuscula Todo menos digitos numericos
resultado2 =re.findall(r'\d',texto)
print(resultado2)

#\w -> busca caracteres alfanumericos [a-z,A-Z,0-9,_] en mayuscula todo menos lo indicado
resultado3 =re.findall(r'\w',texto)
print(resultado3)


