frutas = ["banana","manzana","ciruela",
          "pera","naranja","granada","durazno"]
palabras_cadena = ["hola mundo"]
numeros = [2,5,8,10]

#Evitando que se coma una granada y durazno con la sentencia continue
for fruta in frutas :
    if fruta == "granada" or fruta == "durazno":
        continue
    print(f'Me comere una {fruta}')
    
 #Evitando que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas :
     print(f'Me comere una {fruta}')
     print('------')
     if fruta == 'ciruela':
         break
else: 
    print ("bucle terminado")
    
    
#recorrer una cadena de texto
for letra in palabras_cadena:
    print(letra)
    print("-----")

#operaciones matematicas en lista con for
numeros_duplicados = list() #creo lista vacia
for numero in numeros:
    numeros_duplicados.append(numero*2) #creacion de bucle y agregando con append a la lista vacia
    
print(numeros_duplicados)
print("-------")

#lo anterior resumiendo codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
