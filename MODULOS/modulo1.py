
#import modulo_saludar as modulo_prueba #as te asigana la variable por otra

#saludo = modulo_prueba('Teclado','Alfombra') #al importar se vuelve en metodo
#print(saludo)


#si se necesita llamar la funcion sin que sea todo el modulo

from modulo_saludar import saludar as saludo_antigo,saludar_actual as saludar_como_joven
saludo_1 = saludo_antigo ('Alfombra')
saludo_2 = saludar_como_joven('Cama')
print (saludo_1)
print(saludo_2)

#para ver las propiedades y metodos de el namespace
#print (dir(modulo_saludar))

