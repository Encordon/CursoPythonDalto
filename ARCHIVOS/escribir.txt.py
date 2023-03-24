with open('ARCHIVOS\\prueba_escritura.txt','w',encoding='UTF=8') as X:
  #sobreescribiendo el archivo
  #x.write("jajja te borre el erchivo")
  
  X.writelines(['Esta es la primera linea\n','Esta es la segunda linea\n'
                'Y es la ultima linea\n'])
  
  X.writelines(['Esta es la primera linea\n','Esta es la segunda linea\n'
                'Y es la ultima linea'])