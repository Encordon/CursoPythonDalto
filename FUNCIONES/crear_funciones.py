
#creando una funcion simple
def despedir():
    print("bye bye baby, te vas sin decir adios")
    print('-----')
 
#ejectuando la funcion simple    
despedir()
despedir()

#creando funcion con parametros
def saludar (nombre,sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'reina'
    elif (sexo == 'hombre'):
        adjetivo = 'titan'
    else:
        adjetivo = 'amor'

    print(f"Hola {nombre}, mi {adjetivo} ¿como andas?")

saludar("Camila",'Mujer')
saludar("Enrique","hombre")
saludar("Franes","gay")


#crear funcion que retorne valores
def crea_contraseña_random(num):
  listado_de_caracteres =  "qwertyuiopasdfghjklñzxcvbnm"
  num_entero = str(num)  #transformando num a string
  num = int(num_entero[0]) #tranformando num a entero y cogiendo solo el primer indice
  c1 = num - 2
  c2 = num
  c3 = num - 5
  contraseña = f"{listado_de_caracteres[c1]}{listado_de_caracteres[c2]}{listado_de_caracteres[c3]}{num*2}{num*5}"
  return contraseña,num #convirtiendo a dupla guardando el numero utilizado para la contraseña

#desempaquetando la funcion
password,primer_numero = crea_contraseña_random(456)

#mostrando resultados
frase_usuario = f'Tu contraseña nueva es {password}'
numero_utilizado = f'El numero utilizado es {primer_numero}'
print(frase_usuario)
print(numero_utilizado)