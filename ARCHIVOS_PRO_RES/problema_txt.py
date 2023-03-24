#2 lista una con nombre otra con apellidos

nombre = ['Enrique','Ariana','Pedro','Roberto','Legion']
apellidos = ['Mena','Cordon','Suarez','Alfombra','Asesino']

#Registrar esta inbformacion en TXT

with open("ARCHIVOS_PRO_RES\\problema.txt",'w') as problema:
    problema.writelines('Los datos son:\n')
    [problema.writelines(f'Nombre: {n}\nApellido: {a}\n--------\n') for n,a in zip(nombre,apellidos)]