%matplotlib inline

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from scipy.spatial import distance_matrix
from sklearn.preprocessing import MinMaxScaler

# Para no mostrar 'Future Warnings' producto de que algunos paquetes aún
# trabajan con versiones no actualizadas de otros paquetes
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Lectura del dataset bike
DATOS_BIKE = pd.read_csv('./train-bike.csv', parse_dates=['datetime'])
print(DATOS_BIKE[['temp','windspeed','count']].describe())
DATOS_BIKE['temp_level'] = pd.cut(DATOS_BIKE['temp'], bins=[0,15,30,np.inf], labels=['T1', 'T2', 'T3'])
DATOS_BIKE['wind_level'] = pd.cut(DATOS_BIKE['windspeed'], bins=[-0.5,15,30,45,np.inf], labels=['W1', 'W2', 'W3', 'W4'])
DATOS_BIKE['usage'] =  pd.cut(DATOS_BIKE['count'], bins=[0,20,200,np.inf], labels=['LOW', 'MEDIUM', 'HIGH'])
DATOS_BIKE.info()

# EJERCICIO: histograma con los valores del atributo 'count'
DATOS_BIKE['count'].hist()

# EJERCICIO: diagrama de tarta con la distribución de valores del atributo 'usage'
DATOS_BIKE['usage'].value_counts().plot(kind='pie')

# EJERCICIO: diagrama de puntos para mostar la distribución de 'temp' y 'humidity'
DATOS_BIKE.plot(kind='scatter', x='temp', y='humidity')

# EJERCICIO: diagrama de puntos para mostar la distribución de 'temp' y 'humidity' usando 'count' para la intensidad de color
# Comparar los diagramas generados con las intensidades de color de usuarios ocasionales y registrados
DATOS_BIKE.plot(kind='scatter', x='temp', y='humidity', c='count')

DATOS_BIKE.plot(kind='scatter', x='temp', y='humidity', c='registered')

DATOS_BIKE.plot(kind='scatter', x='temp', y='humidity', c='casual')

# EJERCICIO: repetir el ejercicio anterior cambiando la escala de colores
# Probar distintas combinaciones. Más información en https://matplotlib.org/stable/tutorials/colors/colormaps.html
DATOS_BIKE.plot(kind='scatter', x='temp', y='humidity', c='count', cmap='inferno')

# EJERCICIO: diagrama de celdas para mostrar la distribución de 'temp' y 'humidity'. Probar varios tamaños de celda.
DATOS_BIKE.plot(kind='hexbin', x='temp', y='humidity', gridsize=10)

# EJERCICIO: repetir el ejercicio anterior usando distintas funciones de agregación para determinar la intensidad de color:
#   - Función 'len' sobre 'count' para reproducir el gráfico anterior
#   - Distintas funciones matemáticas sobre el atributo 'count'
DATOS_BIKE.plot(kind='hexbin', x='temp', y='humidity', C='count', gridsize=10, reduce_C_function=np.sum)

# EJERCICIO: genera las gráficas que consideres más interesantes haciendo uso de otros atributos del dataset
# Por ejemplo, puedes visualizar la diferencia de uso de bicicletas entre días festivos y laborables, tanto para usuarios registrados como casuales

'''
PENDIENTE
'''

# días festivos
'''
PENDIENTE
'''

# días laborables
'''
PENDIENTE
'''

# EJERCICIO:  Mostrar el histograma del atributo 'temp'
# Ver la función displot de seaborn
sns.displot(data=DATOS_BIKE, x='temp')

# Otra forma:
sns.displot([DATOS_BIKE['temp']])

# EJERCICIO: Mostrar un diagrama con histograma y estimación KDE de la distribución de probabilidad del atributo 'temp'
sns.displot(data=DATOS_BIKE, x='temp', kde=True)

# EJERCICIO: repetir el ejercicio anterior mostrando solo la estimación de la distribución KDE
sns.displot(data=DATOS_BIKE, x='temp', kind='kde')

# EJERCICIO: Mostrar las distribuciones de probabilidad para la serie temp según las estaciones del año
# (1: primavera, 2:verano, 3:otoño, 4: invierno)
sns.displot(data=DATOS_BIKE, x='temp', hue='season', kind='kde')

# EJERCICIO: Mostrar dos distribuciones de probabilidad para la serie temp según las estaciones del año:
# - Para días festivos y días laborables
sns.displot(data=DATOS_BIKE, x='temp', kind='kde', col='holiday', hue='season')

# EJERCICIO: diagrama 2D con la distribución KDE para dos atributos: 'temp' y 'humidity'
# Ver la función jointplot de seaborn
sns.jointplot(data = DATOS_BIKE, x ='temp', y ='humidity', kind='kde')

# EJERCICIO: diagrama de barras para el atributo discreto 'usage'
# Ver la función countplot de seaborn
sns.countplot(data=DATOS_BIKE, x='usage')

# EJERCICIO: diagrama de barras para el atributo 'usage' detallado según el atributo 'temp_level'
sns.countplot(data=DATOS_BIKE,x='usage',hue='temp_level')

# EJERCICIO: 
#    - Crear una tabla de contingencia con la frecuencia de cada posible pareja de valores de atributos 'temp_level' y 'season'
#      (ver la función crosstab de pandas)
#    - Generar un mapa de calor a partir de la anterior tabla de contingencia
#      (ver la función heatmat de seaborn)
tabla = pd.crosstab(index=DATOS_BIKE['temp_level'],columns=DATOS_BIKE['season'])
print(tabla)
sns.heatmap(tabla,annot=True,fmt='d')

'''
PENDIENTE
'''

# FIN