'''
Alejandro Fernández Trigo
29/03/2022 - IE
'''

#Importaciones

#Tratamiento de dataset
import pandas as pd
import numpy as np

#OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

#Visualización
import matplotlib.pyplot as plt
import seaborn as sns

#Métricas de evaluación
from sklearn import metrics

#Time
import time

# Lee los datos del .csv
DATOS = pd.read_csv('datos/valoraciones.csv')

# Muestra los 5 primeros datos
DATOS[:5]
DATOS.describe()

# Comprueba si hay valores ausente; los muestra:
DATOS.isnull()

# Eliminar filas vacías, obteniendo un conjunto PELICULAS ya filtrado:
PELICULAS = DATOS.dropna()

# Lo compruebo:
PELICULAS.isnull()

# Se puede observar que se han eliminado varias filas:

PELICULAS.head()

# Diagrama de tarta con los generos principales:
PELICULAS['género_principal'].value_counts().plot(kind='pie')

# Diagrama de barras con frecuencia aparación según la recomendación: 
sns.countplot(data=PELICULAS, x='clasificación')

# Los mismo pero con un histograma:
PELICULAS['clasificación'].hist()

# Histograma y estimación KDE de la distribución de probabilidad del atributo valoración:
sns.displot(data=PELICULAS, x='valoración', kde=True, bins = 10)

# Distribución probabilidad atributo duración:
sns.displot(data=PELICULAS, x='clasificación', kde=True)

# Mapa de calor para cada pareja posible de valores (clasificación, género_principal):
tabla_auxiliar = pd.crosstab(index=PELICULAS['clasificación'], columns=PELICULAS['género_principal'])
print(tabla_auxiliar)

# Ahora muestro el mapa de calor asociado:
sns.heatmap(tabla_auxiliar, annot=True, fmt='d')

# Diagrama de cajas para el atributo presupuesto según género_principal:
sns.boxplot(x = PELICULAS['presupuesto'], y = PELICULAS['género_principal'])

'''
Las variables categóricas toman valores fijos; son: género_principal, género_secundario y clasificación.
'''
PELICULAS.head()

DATOS_CATEGORICOS = PELICULAS[['género_principal', 'género_secundario', 'clasificación']]
DATOS_CATEGORICOS.head()

'''
Este bucle imprime un DataFrame que muestra los tres datos categóricos, junto al nº de posibles valores que toman y una lista
de esos posibles x valores (llamados niveles).
'''
niveles = pd.DataFrame(columns = ['Números', 'Niveles'])

for atributo in DATOS_CATEGORICOS.columns.values:
    valores = list(DATOS_CATEGORICOS[atributo].value_counts().keys())
    niveles.loc[atributo] = (len(valores), valores)
    
niveles

# Codificación label encoding para el atributo clasificación:
# Comentado porque me da problemas al ejecutarlo:

'''
PELICULAS['clasificación-label'] = PELICULAS['clasificación'].map({'PG-13' : 'Parents Strongly Cautioned', 'G' : 'General audiences', 'R' : 'Restricted', 'PG' : 'Parental Guidande Suggested'})
DATOS.head()
'''

# Codificación one hot encoding para los atributos género_principal y género_secundario:
PELICULAS = pd.get_dummies(PELICULAS, columns = ['género_principal'])
PELICULAS = pd.get_dummies(PELICULAS, columns = ['género_secundario'])
PELICULAS.head()

'''
Un clasificador nos responde a una pregunta de SI/NO (por ejemplo), por ejemplo, para el ejemplo visto de tratamiento de 
cáncer, tiene sentido usar clasificación ante una pregunta del tipo "¿Este cáncer es benigno o no?". Pero en el caso de 
películas, tiene más sentido una regresión ya que su salida será un número; nos permite preguntar: "¿Cuanto recaudará en
taquilla?" (por ejemplo).
'''
PELICULAS.head()

# Preparar el conjunto; usamos el atributo valoración:
'''
X es el conjunto, y la serie de valoraciones.
Elimino todos los valores que no sean numéricos; además del atributo valoración.
'''
X_1 = PELICULAS.drop(['valoración'], axis = 1)
X_2 = X_1.drop(['género_principal'], axis = 1)
X_3 = X_2.drop(['género_secundario'], axis = 1)
X = X_3.drop(['clasificación'], axis = 1)

y = PELICULAS['valoración']

X.head()

# Crear un DataFrame para almacenar los resultados que tenga dos columnas: evaluación, tiempo:
RESULTADOS = pd.DataFrame(columns=['EVALUACIÓN', 'TIEMPO'])
RESULTADOS

'''
Definir una función que realice un experimento, a partir de un estimador concreto. La función devolverá el valor de la 
medida de evaluación elegida y el tiempo empleado, con una validación cruzada de 10 particiones.
'''
from sklearn.linear_model import LinearRegression
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score, learning_curve

# Definición del clasificador 
clasificador = LinearRegression()
clasificador.fit(X,y)

# Con el clasificador creado, hacer validación cruzada de 10 participantes:
y_pred_cross = cross_val_predict(clasificador, X, y, cv = 10)

# Definicion de la función, recibe el clasificador, X y recibirá y_pred_cross:
def experimento(clasificador, X, y):
    
    # Tiempo inicio:
    tini = time.time()
    
    y_pred = cross_val_predict(clasificador, X, y)
    f1 = f1_score(y, y_pred)
    
    # Tiempo fin:
    tfin = time.time()
    
    return (f1, tfin - tini)

'''
Añadir a la tabla de resultados al menos 5 líneas en las que se prueben 5 estimadores diferentes 
(o algunos iguales con distinta parametrización)
'''

# Estimadores:
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor

# Añadir a la tabla creada previamente los resultados de aplicar la función antes definida con dichos estimadores:
# Algo aquí se está usando mal y da errores.
RESULTADOS.loc['LogRegr'] = experimento(LinearRegression(), X, y)
RESULTADOS.loc['Kneigh-3'] = experimento(KNeighborsRegressor(3), X, y)
RESULTADOS.loc['Kneigh-5'] = experimento(KNeighborsRegressor(5), X, y)
RESULTADOS.loc['DTree'] = experimento(DecisionTreeRegressor(), X, y)
RESULTADOS.loc['GBoost'] = experimento(GradientBoostingRegressor(), X, y)

RESULTADOS

# FIN