frase = input('Dime una frase y te calculo cuanto tardas en decirla: ')
palabras_separadas = frase.split(" ") #transforma la frase en lista con cada espacio en blanco
cantidad_de_palabras = len(palabras_separadas) #cuenta elementos en una lista
tiempo_por_palabras = cantidad_de_palabras/2


print(f'Has dicho {cantidad_de_palabras} palabras, y tardarias {tiempo_por_palabras} segundos en decirlo ')
print(f'Dalto lo diria {tiempo_por_palabras*0.7} segundo en decirlo')

if cantidad_de_palabras > 60:
    print ('Que haces! no te pedi un testamento')
else : print ('Eres un buen orador')





