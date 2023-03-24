ingreso_mensual = 1250
gasto_mensual = 1000
Money = ingreso_mensual - gasto_mensual 

if ingreso_mensual >= 1000:
    print ("estas bien economicamente en latinoamerica")
    if Money < 0:
        print ("No terminas el mes")
    elif Money >= 100:
        x = f"Te sobra = {Money}"
        print (x)
        
    else :
        print ("Revisar gastos")
elif ingreso_mensual > 10000:
    print ("estas bien economicamente en cualquier parte del mundo")


elif ingreso_mensual > 500:
    print ("estas bien economicamente en Argentina")
    
elif ingreso_mensual > 200:
    print ("estas bien economicamente en Nicaragua")


else:
    print ("puto pobre")    