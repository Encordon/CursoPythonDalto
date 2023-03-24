import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ARCHIVO_PRO_GRAF\\pedos.csv')
sns.lineplot(x='fecha',y='pedos',data=df)

#creando un punto en las coordenadas x,y
plt.plot('01-09',17,'o')

plt.show()
