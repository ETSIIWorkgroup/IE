import numpy as np
import pandas as pd

# EJERCICIO: crear dos series con los números del 1 al 5
#    - numeros: con el índice por defecto
#    - numeros_ix_ch: usando como índices las vocales = ['a', 'e', 'i', 'o', 'u']
numeros = pd.Series([1, 2, 3, 4, 5])
numeros

numeros_ix_ch = pd.Series([1, 2, 3, 4, 5], ['a', 'e', 'i', 'o', 'u'])
numeros_ix_ch

# EJERCICIO: crear dos dataframes de la siguiente matriz de números aleatorios 'np.random.rand(10,3)'
#    - df: sin especificar nombres de columnas
#    - df_col: usando como nombres de columnas ['C1', 'C2', 'C3']
df = pd.DataFrame(np.random.rand(10,3))
df

df_col = pd.DataFrame(np.random.rand(10,3), columns=['C1', 'C2', 'C3'])
df_col

# EJERCICIO: mostrar el resultado de las siguientes consultas sobre series
#    - elemento 0 de la serie 'numeros'
#    - serie con los elementos 1-3 de la serie 'numeros'
#    - elemento de la serie 'numeros_ix_ch' indexado con el carácter 'e'
#    - serie con los elementos de la serie 'numeros' que sean mayores que 3
numeros
numeros_ix_ch

numeros[0]
numeros[1:4]
numeros_ix_ch['e']
resultado = pd.Series([i for i in numeros if i > 3])
resultado

# EJERCICIO: mostrar el resultado de las siguientes consultas sobre dataframes
#    - fila 3 del dataframe 'df'
#    - fila 3 del dataframe 'df_col'
#    - columna 1 de la fila 3 del dataframe 'df'
#    - columna 'C1' del dataframe df_col
df
df_col

df.iloc[3]
df_col.iloc[3]
df.iloc[3].get(1)
df_col.get('C1')

# EJERCICIO: mostrar el resultado de los siguientes consultas sobre dataframes
#    - dataframe compuesto por las columnas 'C1' y 'C3' del dataframe 'df_col'
#    - dataframe compuesto por las filas del dataframe 'df_col' cuyo valor de 'C2' sea mayor que 0.5
#    - dataframe compuesto por las columnas 'C1' y 'C3', con las filas cuyo valor de 'C2' sea mayor que 0.5
#    - dataframe con todas las columnas y con las filas en las que 'C2' sea mayor que 0.5 y 'C3' sea menor que 0.5
df_col

# dataframe compuesto por las columnas 'C1' y 'C3' del dataframe 'df_col'
df13 = pd.DataFrame(columns = [df_col.get('C1'), df_col.get('C3')])
df13

# dataframe compuesto por las filas del dataframe 'df_col' cuyo valor de 'C2' sea mayor que 0.5
df_col[df_col['C2'] > 0.5]

# dataframe compuesto por las columnas 'C1' y 'C3', con las filas cuyo valor de 'C2' sea mayor que 0.5
df_col[df_col['C2'] > 0.5][['C1', 'C3']]

# dataframe con todas las columnas y con las filas en las que 'C2' sea mayor que 0.5 y 'C3' sea menor que 0.5
df_col[(df_col['C2'] > 0.5) & (df_col['C3'] < 0.5)]

'''
Los datos que utilizaremos a continuación han sido obtenidos de Capital bikeshare (https://ride.capitalbikeshare.com/system-data), a través de kaggle: https://www.kaggle.com/c/bike-sharing-demand/overview/

Haremos uso del conjunto de entrenamiento proporcionado, que se compone de los primeros 19 días de cada mes, mientras que el conjunto de prueba es del 20 al final del mes.
'''

# EJERCICIO: leer el fichero de datos './train-bike.csv' en un dataframe
BIKE = pd.read_csv('./train-bike.csv')
BIKE[:5]

# EJERCICIO: probar los métodos de los dataframes para las siguientes operaciones:
#    - Mostrar información sobre las columnas
#    - Mostrar indicadores estadísticos sobre las columnas
#    - Mostrar los tipos de las columnas
#    - Obtener una matriz numpy con los valores de los datos
BIKE.info()

BIKE.describe()

BIKE.dtypes

BIKE.values

# Adicional 
# - Shape (nº filas + columnas)
# - Columns (columnas y sus valores)
BIKE.shape
BIKE.columns
BIKE.columns.values

# EJERCICIO: realizar las siguientes consultas sobre el dataframe con los datos de bike
#    - contar cuántas ocurrencias de cada valor del atributo season hay en el dataset.
#    - dividir el rango de valores de temp en diez partes y calcular cuántos elementos hay en cada uno de esos segmentos. 
BIKE['season'].value_counts()

# BIKE['temp'].value_counts()
pd.cut(BIKE['temp'], 10).value_counts()

# EJERCICIO: realizar las siguientes consultas sobre el dataframe con los datos de bike
#    - crear un atributo temp_wind que se calcule mediante la diferencia entre temp y windspeed.
#    - normalizar (de 0 a 1) las columnas season y weather guardándolas en las columnas 'season_norm' y 'weather_norm'.
#    La normalización la llevaremos a cabo dividiendo cada elemento por el máximo de los valores de su columna
BIKE['temp_wind'] = BIKE['temp'] - BIKE['windspeed']
BIKE['temp_wind']
BIKE

'''
PENDIENTE!
'''

# FIN