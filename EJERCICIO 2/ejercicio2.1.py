#falto el profe y los pibes van armar la clase

#pedir el nombre y la edad de los compañeros que vinieron hoy a clases

#funcion para obtener al asistente y el profesor segun la edad
def obtener_compañeros (cantidad):
    
    #creando la lista de compañeros
    compañeros = []
    
    #ejecutando un for para pedir la informacion de los compañeros
    for i in range(cantidad):
        nombre = input("ingrese el nombre del compañero:   ")
        edad = int(input('ingrese la edad del compañero:   '))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista compañeros[]
        compañeros.append(compañero)
        
    #ordenando de menor a mayor segun su edad    
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad)
    asistente = compañeros [0][0]
    profesor = compañeros [-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(3)
        
print(f'El profesor es: {profesor} y su asistente es {asistente}')        