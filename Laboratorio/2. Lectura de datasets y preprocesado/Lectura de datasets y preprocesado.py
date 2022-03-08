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

# normalizar (de 0 a 1) las columnas season y weather guardándolas en las columnas 'season_norm' y 'weather_norm'
'''
ERROR - PENDIENTE DE ARREGLAR!
'''

BIKE['season_norm'] = BIKE['season'].value_counts(normalize=True)
BIKE['weather_norm'] = BIKE['weather'].value_counts(normalize=True)
BIKE

# EJERCICIO: crear un dataframe con los atributos weather y humidity, con los registros de los datasets train y test.
BIKE_TEST = pd.read_csv('./test-bike.csv')
BIKE_TEST.info()

BIKE_TT = pd.concat([BIKE[['weather', 'humidity']], BIKE_TEST[['weather', 'humidity']]])
BIKE_TT.info()
BIKE_TT.head()

# EJERCICIO: definir una función calcula_level que devuelva los siguientes valores
# a partir de una temperatura:
#      'T1' para temperaturas menores a 15
#      'T2' para temperaturas mayores o iguales que 15 y menores que 30
#      'T3' para temperaturas mayores o iguales que 30
def calcula_level(temp):
    if temp < 15:
        return 'T1'
    elif (temp >= 15 and temp < 30):
        return 'T2'
    else:
        return 'T3'

# crear un atributo 'temp_level' segmentando el atributo 'temp' usando la función calcula_level 
BIKE['temp_level'] = BIKE['temp'].apply(calcula_level)
BIKE.head()

# EJERCICIO: crear el atributo temp_code a partir del atributo numérico temp_level que toma los valores 1, 2 y 3 (usando map)
# Es posible porque existe un orden implícto
BIKE['temp_code']= BIKE['temp_level'].map({'T1':1, 'T2':2, 'T3':3})
BIKE['temp_code'].value_counts()

# Es un string
BIKE.iloc[0,0]

# EJERCICIO: volver a leer el dataset train analizando los datos tipo fecha y generar dos nuevas columnas:
#    - dia: con el día de la fecha
#    - mes: con el mes de la fecha
BIKE_F = pd.read_csv('./test-bike.csv', parse_dates=['datetime'])
BIKE_F.info()
BIKE_F.head()

BIKE_F['dia'] = BIKE_F['datetime'].dt.day
BIKE_F['mes'] = BIKE_F['datetime'].dt.month
BIKE_F.head()

# EJERCICIO: normalizar los valores de 'temp' entre [0,1] con la técnica _min-max_ y guardarlos en la columna 'temp_mm'
# Media: mean() Desv. standar: std()
# Min: min() Max: max()

valor_min = BIKE_F['temp'].min()
valor_max = BIKE_F['temp'].max()
media = BIKE_F['temp'].mean()
desviacion = BIKE_F['temp'].std()

diff = BIKE_F['temp'].max() - BIKE_F['temp'].min()
BIKE_F['temp_mm'] = (BIKE_F['temp'] - BIKE_F['temp'].min()) / diff
BIKE_F.head()

print(valor_min)
print(valor_max)
print(media)
print(desviacion)
print(diff)

# EJERCICIO: 
#    - Normalizar los valores de 'registered' con la técnica z-score y guardarlos en la columna 'registered_zs'
#    - Comparar la media y la desviación estándar de ambas columnas
BIKE['registered_zs'] = (BIKE['registered'] - BIKE['registered'].mean()) / BIKE['registered'].std()
BIKE.head()

# EJERCICIO: importar desde sklearn los elementos que necesitemos
from sklearn.preprocessing import MaxAbsScaler, MinMaxScaler, StandardScaler

# EJERCICIO: aplicar las transformacines necesarias para crear las siguientes columnas
#    - registered_maxabs: MaxAbsScaler sobre la columna 'registered'
#    - registered_minmax: MinMaxScaler sobre la columna 'registered'
#    - registered_sca: StandardScaler sobre la columna 'registered'

'''
Fit ajusta los datos pero NO devuelve nada, a diferencia de transform.
'''

#    - registered_maxabs: MaxAbsScaler sobre la columna 'registered'
# Objeto que normaliza los datos que reciba; entrada: una matriz
normalizador = MaxAbsScaler()
normalizador.fit(BIKE[['registered']])

# La transformación genera una salida que será una nueva columna:
BIKE['registered_maxabs'] = normalizador.transform(BIKE[['registered']])
BIKE.head()

# - registered_minmax: MinMaxScaler sobre la columna 'registered'
# Más rápido invocando al método combinado que hace fit y transform a la vez:
BIKE['registered_minmax'] = MinMaxScaler().fit_transform(BIKE[['registered']])
BIKE.head()

# - registered_sca: StandardScaler sobre la columna 'registered'
BIKE['registered_standard'] = StandardScaler().fit_transform(BIKE[['registered']])
BIKE.head()

# Cargamos los datos de 'weather.csv' en el dataframe 'DATOS'
DATOS = pd.read_csv('./weather.csv')
DATOS.info()
DATOS.head()

# EJERCICIO: crear las matrices 'DATOS_discretos' y 'DATOS_numericos' con los atributos discretos y numéricos, respectivamente, de 'DATOS'
# Dos formas de crear las matrices:
DATOS_discretos = DATOS[['outlook', 'windy', 'play']]
DATOS_discretos.head()

DATOS_numericos = DATOS.select_dtypes(include=['int64'])
DATOS_numericos.head()

# EJERCICIO: mostrar el número de 'levels' para cada atributo discreto
# Crear un DataFrame con las columnas 'Número' y 'Niveles'
# Añadir una fila para cada atributo discreto con el número de posibles valores y sus valores
niveles = pd.DataFrame(columns = ['Números', 'Niveles'])

for atributo in DATOS_discretos.columns.values:
    valores = list(DATOS_discretos[atributo].value_counts().keys())
    niveles.loc[atributo] = (len(valores), valores)
    
niveles

# DATOS_discretos.columns.values
# DATOS_discretos['outlook'].value_counts()

# EJERCICIO: codificar mediante label encoding el atributo 'play' en una nueva columna 'play_label', usando map
DATOS['play_label'] = DATOS['play'].map({'yes' : 1, 'no' : 0})
DATOS.head()

# EJERCICIO: codificar mediante one hot encoding el atributo categórico 'outlook'
#    - Pandas proporciona un método para hacerlo
DATOS = pd.get_dummies(DATOS, columns = ['outlook'])
DATOS.head()

# Cargamos los datos de 'titanic.csv' en el dataframe 'TITANIC'
DATOS = pd.read_csv('./titanic.csv')
DATOS.head()

# EJERCICIO: mostrar aquellas filas que contengan algún valor ausente
DATOS.isnull()

# Otra forma: vemos que columnas contienen valores nulos:
DATOS.isnull().any(axis=0)

# Si quiero verlo por filas:
DATOS.isnull().any(axis=1)

# Si quiero verlo como dataframe:
DATOS[DATOS.isnull().any(axis=1)].head()

# EJERCICIO: Crear un dataframe TITANIC2 donde se hayan eliminado todas las filas con valores ausentes
DATOS2 = DATOS.dropna()
print(DATOS2.shape)
DATOS2.head()

# EJERCICIO: Crear un dataframe TITANIC3 a partir del original donde:
# - Se elimine la columna cabin (es la que más NaN tiene)
# - Se eliminen aquellas filas con valores ausentes (una vez eliminada cabin)
DATOS3 = DATOS.drop(['cabin'], axis=1)
DATOS3.head()

DATOS3.dropna(inplace=True)
DATOS3.head()

# EJERCICIO: construir las siguientes columnas en la que se sustituyen los valores NaN de la forma en que se indica:
#    - 'age_fill' sustituyendo los valores NaN de 'age' con la media de la columna
#    - 'fare_fill' sustituyendo los valores NaN de 'fare' con la media de la columna
#    - 'cabin_fill' sustituyendo los valores NaN de 'cabin' con el valor más frecuente de la columna (moda)
#    - 'embarked_fill' sustituyendo los valores NaN de 'embarked' con el valor más frecuente de la columna (moda)

# Para poder usar la moda:
from statistics import mode

DATOS3['age_fill'] = DATOS3['age'].fillna(DATOS3['age'].mean())
DATOS3['fare_fill'] = DATOS3['fare'].fillna(DATOS3['fare'].mean())
DATOS3.head()

# DATOS3['cabin_fill'] = DATOS2['cabin'].fillna(DATOS3['cabin'].mode()[0])
DATOS3['embarked_fill'] = DATOS2['embarked'].fillna(DATOS3['embarked'].mode()[0])
DATOS3.head()

# EJERCICIO: Crear un DataFrame TITANIC4 a partir del anterior borrando las columnas con datos ausentes
DATOS3.dropna(axis=1, inplace=True)
DATOS3.head()

# FIN