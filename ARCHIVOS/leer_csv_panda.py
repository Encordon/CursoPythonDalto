import pandas as pd

#usando la funcion read_csv para leer el archivo csv
df = pd.read_csv('ARCHIVOS\\datos.csv')
df2 = pd.read_csv('ARCHIVOS\\datos.csv')

#obteniendo los datos de la columna nombre
nombres = df['nombre']
print(nombres)
print('-----')

#ordenando el dataframe por la edad
df_ordenado = df.sort_values('edad')

#ordenando el dataframe por la edad de forma descendente
df_orden_descendete = df.sort_values('edad',ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 filas con head()
primeras_filas = df.head(3)

#accediendo a las primeras 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
numero_filas,nuemero_columnas = df.shape

#obteniendo datos estadistica del dataframe
df_info = df.describe()

#accediendo a un elemento especifico del df con loc (fila 2, columna edad)
elemento_especifico_loc = df.loc[2,'edad']

#accediendo a un elemento especifico del df con iloc (fila 2, columna 2)
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df['edad']>30,:]


print(mayor_que_30)