#abriendo el archivo con with open
with open('ARCHIVOS\\prueba.txt',encoding='UTF=8') as X:
    #leemos el archivo
    
    contenido = X.read()
    print(contenido)
    
#no es necesario cerrarlo con with open