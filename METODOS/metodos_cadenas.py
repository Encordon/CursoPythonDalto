cadena1 = "Hola soy el futuro5"
cadena2 = "Bienvenido IA"

print(dir(cadena1)) #con dir se puede saber las cosas que se puede hacer con el elemento

#X = Dato .(metodo) #sintaxis del metodo

Mayusc = cadena1.upper() #convierte en mayuscula
Minusc = cadena1.lower() #convierte en minuscula
primera_letra_en_Mayusc = cadena1.capitalize() #primera letra en mayuscula


busqueda_find = cadena1.find("a") #busca una cadena en otra cadena
#indica numero de posicion empezando de 0, si no hay concidencias devuelve -1
busqueda_index = cadena1.index("a")#busca una cadena en otra cadena
#indica numero de posicion empezando de 0, si no hay concidencias devuelve una excepcion


es_numerico = cadena1.isnumeric() #si es numerico (solo numeros) devuelve true, si no false
es_alphanumerico = cadena1.isalpha() #si es alfanumerico (caracteres de la A a la Z y Numeros 0 al 9) devuelve true, si no false


contar_coincidencias = cadena1.count("o") #cuenta la cantidad de veces que coincide
contar_caracteres = len(cadena1) #cuenta la cantidad de caracteres dentro de una cadena (es una FUNCION)


empieza_con = cadena1.startswith("H") #verifica s una cadena empieza con otra cadena dada, si es asi devulve true
termina_con = cadena1.endswith("5") #verifica si una cadena termina con otra cadena dada, si es asi devuelve true


cadena_nueva = cadena1.replace("o", "e") #si el calor1, se encuentra en la cadena original, remplaza el valo inicial por el final
cadena_separada = cadena1.split(" ")

print (Mayusc)
print (Minusc)
print (primera_letra_en_Mayusc)

print (busqueda_find)
print (busqueda_index)

print (es_numerico)
print (es_alphanumerico)

print (contar_coincidencias)
print (contar_caracteres)

print (empieza_con)
print (termina_con)

print (cadena_nueva)
print (cadena_separada)