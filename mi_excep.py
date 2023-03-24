#creando mi propia excepcion
class Miexpeccion(Exception):
    def __init__(self,err):
        print(f'Impresionante,cometiste el siguiente error: {err}')
        
#Lanzando mi propia excepcion
#raise Miexpeccion('Error, fallo en la matrix')

try:
    raise Miexpeccion('Error, fallo en la matrix')
except:
      print('No seas pendejo')