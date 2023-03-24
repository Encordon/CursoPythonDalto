

#usando open para abrir el archivo y codificacion universal (UTF(8))
archivo = open('ARCHIVOS\\prueba.txt',encoding='UTF=8')

#leer archivo completo (no se puede volver a leer)
leer = archivo.read()
archivo.close()
print(leer)
print('------')

archivo = open('ARCHIVOS\\prueba.txt',encoding='UTF=8')
#leer linea por linea
lineas =archivo.readlines()
archivo.close()
print(lineas)
print('------')

archivo = open('ARCHIVOS\\prueba.txt',encoding='UTF=8')
linea1 = archivo.readline()
archivo.close()
print(linea1)
print('------')