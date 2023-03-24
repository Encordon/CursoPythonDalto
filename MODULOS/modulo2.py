#si el modilo estuviera dentro de una carpeta en la misma ruta se va conn .
#import Funcionesbuenas.saludar as Saludo_corto

#print(Saludo_corto.saludar('Alfombra'))

import sys

a = sys.path # con esto se ve la ruta de la carpeta
#print(a)

sys.path.append('c:\\Users\\34695\\Desktop\\curwso pyton\\Funcionesbuenas')
import saludar as saludo_cambiado #importamos modulo y asiganmos otro nombre
 
print (saludo_cambiado.saludar_actual('Alfombra')) #print modulo con nuevo nombre.funcion
print (saludo_cambiado.saludar('teclado'))


