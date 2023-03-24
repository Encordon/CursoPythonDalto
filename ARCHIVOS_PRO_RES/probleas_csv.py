
#abrir archivo
import pandas as pd
df = pd.read_csv('ARCHIVOS_PRO_RES\\datos.csv')

#converit a string los datos de columna
df['edad'] = df ['edad'].astype(str)

#remplazando los datos
df['nombre'].replace('Enrique', 'Crack',inplace=True)

print(df)

#eliminando  filas con datos faltantes
df = df.dropna()

#eliminando filas repetidas
df =df.drop_duplicates()


#creando un CSV con el dataframe resultante
df.to_csv('ARCHIVOS_PRO_RES\\datos_actualizados.csv')