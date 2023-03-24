#creando una funcion que muestre la serie de fibonacci entre el 0 el numero dado


def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num:
            return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b, a+b

resultado = fibonacci (78)
print (resultado)