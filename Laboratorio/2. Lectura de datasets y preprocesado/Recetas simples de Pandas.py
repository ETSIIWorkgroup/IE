import pandas as pd
import numpy as np

numeros = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
numeros

numeros * 2

numeros - (numeros * 2)

numeros[numeros%2==0]

def triple(x):
    return 3*x
numeros.apply(triple)

df = pd.DataFrame(np.random.rand(10,3), columns=['A', 'B', 'C'])
df

df['A']

df['C'] = df['A']-df['B']

df[['C', 'B']]

df[['A']]

df[df['C']>0.2].A

BIKE = pd.read_csv('./train-bike.csv')
BIKE[:10]

# FIN