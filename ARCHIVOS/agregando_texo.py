with open('ARCHIVOS\\prueba_escritura.txt','a',encoding='UTF=8') as X:
#agregando lineas (sin sobreescribir) 
    
    X.write('\n') #agregando linea vacia
    
    #creacion bucle
    for i in range(4):
        X.write(f'Agrego Linea {i+1}\n')