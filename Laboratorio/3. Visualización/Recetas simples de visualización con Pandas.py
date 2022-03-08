%matplotlib inline

import pandas as pd
import numpy as np

numeros = pd.Series([1, 2, 4, 7, 4, 6, 7, 9])
numeros.plot()

numeros = pd.Series(np.random.normal(0,1,10000))
numeros.hist()

xs = np.random.rand(100)
ys = np.random.rand(100)
puntos = pd.DataFrame({'x':xs, 'y':ys})

puntos.plot.scatter(x='x', y='y')

numeros = np.random.rand(50)
etiquetas = pd.Series(pd.cut(numeros, 3, labels=['bajo', 'medio', 'alto']))
etiquetas[:5]

frecuencias = etiquetas.value_counts()
frecuencias

frecuencias.plot(kind='bar', color='green')

# FIN