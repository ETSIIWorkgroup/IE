import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Numpy, scipy y pandas
import numpy as np
import scipy.stats
import pandas as pd

# Datasets
from sklearn.datasets import load_breast_cancer

# Evaluación
from sklearn import metrics
from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score, learning_curve

# Visualización
import seaborn as sns
from pySankey import sankey     # pip install pySankey
import matplotlib.pyplot as plt

print("All done!")

%matplotlib inline

# EJERCICIO: acceder al dataset disponible en sklearn y crear el dataframe 'X' para los atributos, y la serie 'y' para la clase
#    - Mostrar información sobre las columnas
#    - Mostrar con una gráfica la distribución de los valores de la clase
X, y = load_breast_cancer(return_X_y = True, as_frame = True)

X.head()
X.info()
y.value_counts()
y.hist()

'''
1. Entrenar el clasificador con X,y.
2. Separar X_80, y_80 (para entrenar) y X_20, y_20 (para validar).
3. Validación cruzada (porque es un conjunto demasiado pequeño); separando por distintos conjuntos (apartado 2 repetido varias veces).
'''

# EJERCICIO: crear un estimador de la clase LogisticRegression y entrenarlo con el dataset <X,y>
from sklearn.linear_model import LogisticRegression

# Sin el parámetro liblinear necesita más iteraciones, provocaría un fallo.
clasificador = LogisticRegression(solver = 'liblinear')
clasificador.fit(X,y)

# EJERCICIO: predecir la salida de los primeros 10 valores de X con el clasificador entrenado anteriormente
y_pred = clasificador.predict(X)

# Comparar las etiquetas predichas con las reales:
print(y_pred[:10])
print(y[:10])

# Vemos que en el 4º, falla.

# Precisión de la predicción:
metrics.accuracy_score(y, y_pred)

# EJERCICIO: dividir el dataset <X, y> en dos datasets <X_train, y_train> y <X_test, y_test> con una distribución 80%-20%,
#            entrenar el clasificador con <X_train, y_train> y calcular la métrica accuracy con <X_test, y_test>
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Entrenar 
clasificador.fit(X_train,y_train)

# Validar 
y_pred_2 = clasificador.predict(X_test)
print(y_pred_2[:10])
print(y_test[:10])

# Precisión:
metrics.accuracy_score(y_test, y_pred_2)

# Si se ejecuta más veces, se ve que la precisión es poco estable (cambia mucho).

# EJERCICIO: calcular las probabilidades de cada clase para las instancias de X_test y guardarlas en y_test_proba
y_test_prob = clasificador.predict_proba(X_test)
print(y_test_prob[:10])

# EJERCICIO: mostrar con un histograma la distribución de la probabilidad de pertenecer a la clase 1
y_test_proba_1 = pd.Series(y_test_prob[:, 1])
y_test_proba_1.hist()

# EJERCICIO: predecir la salida de todas las instancias mediante validación cruzada y guardar las prediccciones en y_pred
y_pred_cross = cross_val_predict(clasificador, X, y, cv = 10)  # cv es el nº de particiones
print(y_pred_cross[:10])
print("")

# Precisión
print(metrics.accuracy_score(y, y_pred_cross))
print("")

# Si se ejecuta más veces, se ve que la precisión es más estable.

# Otra forma: devuelve un array de precisiones de cada conjunto:
scores = cross_val_score(clasificador, X, y, cv = 10)
print(scores)
print("")

# Si hacemos la media:
print(scores.mean())

# Para usar accuracy_score sin llamar a la librería:
from sklearn.metrics import accuracy_score

# EJERCICIO: calcular las probabilidades de cada clase para todas las instancias y guardarlas en y_pred_prob
y_pred_prob = cross_val_predict(clasificador, X, y, cv=10, method = "predict_proba")
y_pred_prob[:10]

# EJERCICIO: mostrar con un histograma la distribución de la probabilidad de pertenecer a la clase 1 
y_pred_proba_1 = pd.Series(y_pred_prob[:,1]) # Predicción del ejercicio anterior
y_pred_proba_1.hist()

'''
Accuracy = (TP + TN) / N

Precisión = TP / (TP + FP)

Cobertura (o recall) = TP / (TP + FN)

F1 = (2 * Precisión * Cobertura) / (Precisión + Cobertura)
'''

# EJERCICIO: crear la matriz de confusión a partir de 'y' e 'y_pred' en un DataFrame con esta estructura:
#   - Columnas: [Predicted 0, Predicted 1]
#   - Índice: [True 0,True 1]
# Usamos y_pred_cross, que es la ultima evaluación cruzada hecha.

cm = pd.DataFrame(metrics.confusion_matrix(y, y_pred_cross), columns = ["Pred0", "Pred1"], index = ["True0", "True1"])
cm

# EJERCICIO: mostrar la matriz de confusión mediante un mapa de calor de Seaborn
sns.heatmap(cm, annot = True, fmt = "d", cmap = "Blues")

# EJERCICIO: calcular TP, FP, TN y FN a partir de la matriz de confusión anterior
#cm = metrics.confusion_matrix(y, y_pred)
# Accedemos con iloc si usamos el dataframe anterior:
TP = cm.iloc[1,1]
FP = cm.iloc[0,1]
TN = cm.iloc[0,0]
FN = cm.iloc[1,0]

print(str(TP))
print(str(FP))
print(str(TN))
print(str(FN))

# "Invertir la clasificación": calcular la precisión para la clase negativa:
metrics.classification_report(y, y_pred_cross, output_dict = True)

from sklearn.metrics import precision_score, recall_score, f1_score
# Volvemos a usar y_pred_cross como ultima predicción cruzada:

# EJERCICIO: calcular la medida 'precisión' a partir de 'y' e 'y_pred'
pr = TP / (TP + FP)
print(pr)

# Comparación con la precisión de metrics:
metrics.precision_score(y, y_pred_cross)

# EJERCICIO: calcular la medida 'cobertura' a partir de 'y' e 'y_pred'
recall_score(y, y_pred_cross)

# EJERCICIO: calcular la medida 'f1' a partir de 'y' e 'y_pred'
f1_score(y, y_pred_cross)

# DataFrame donde iremos guardando los resultados de los experimentos
RESULTADOS_CLF = pd.DataFrame(columns=['ACCURACY', 'F1', 'TIEMPO'])
RESULTADOS_CLF

# EJERCICIO: implementar la función 'experimento_clf' que encapsule todos los pasos de un experimento de clasificación
#    PARÁMETROS DE ENTRADA:
#       - clasificador: estimador usado en el experimento
#       - X: matriz de atributos
#       - y: vector de salida
#    SALIDAS:
#       - Tupla (accuracy, f1, tiempo) con las métricas del experimento y el tiempo invertido en segundos
def experimento_clf(clasificador, X, y):
    
    # Tiempo inicio:
    tini = time.time()
    
    # Precisión, f1:
    y_pred = cross_val_predict(clasificador, X, y)
    accuracy = accuracy_score(y, y_pred)
    f1 = f1_score(y, y_pred)
    
    # Tiempo fin:
    tfin = time.time()
    
    return (accuracy, f1, tfin - tini)

# EJERCICIO: usar la función 'experimento_clasificacion' con los siguientes clasificadores y almacenar los resultados 
#            en el dataframe RESULTADOS_CLF:
# - Regresión logística
# - Vecinos más cercanos, con k=3 y k=5
# - Árbol de decisión
# - Gradient boosting
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier

RESULTADOS_CLF.loc['LogRegr'] = experimento_clf(LogisticRegression(solver="liblinear"), X, y)
RESULTADOS_CLF.loc['Kneigh-3'] = experimento_clf(KNeighborsClassifier(3), X, y)
RESULTADOS_CLF.loc['Kneigh-5'] = experimento_clf(KNeighborsClassifier(5), X, y)
RESULTADOS_CLF.loc['DTree'] = experimento_clf(DecisionTreeClassifier(), X, y)
RESULTADOS_CLF.loc['GBoost'] = experimento_clf(GradientBoostingClassifier(), X, y)

RESULTADOS_CLF

# EJERCICIO: leer el fichero 'concrete.csv' y crear el dataframe 'X' para los atributos, y la serie 'y' para la clase (atributo 'Concrete compressive strength')
DATOS_CONCRETE = pd.read_csv('./Concrete.csv')
DATOS_CONCRETE.head()

# Eliminamos "Concrete compressive strength" de X, lo ponemos en y:
X = DATOS_CONCRETE.drop(['Concrete compressive strength'], axis = 1)
y = DATOS_CONCRETE['Concrete compressive strength']

X.info()
y
