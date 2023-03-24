def sumar_dos_num():
    while True:
        a = input ('Numero 1 : ')
        b = input ('Numero 2 : ')
        try:
            resultado = int(a) + int(b)
            break
        except Exception as e:
            print('Solo introduzca numeros')
            print(f'Error:{type(e).__name__}') #de esta menra sabemos el nombre del error
        else:
            break
        finally:
            print("Manejo de excepcion finalizado")
        
    return resultado

print(sumar_dos_num())