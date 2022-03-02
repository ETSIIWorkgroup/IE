# Definición de la función doble, que devuelve el parámetro recibido multiplicado por 2 
def doble(x):
    return x*2

# Llamada a la función doble con el parámetro 2
doble(2)

# Llamada a la función doble con el parámetro 'Hola '
doble('Hola')

# Llamada a la función doble con el parámetro [1, 's', 'hola']
doble([1, 's', 'hola'])

# Definición de la función doble_lista mediante iteración. La función recibe una lista como parámetro,
# y devuelve otra lista en el que cada elemento de la lista original ha sido multiplicado por 2.
def doble_lista(lista):
    res = []
    for i in range(len(lista)):
        res.append(lista[i] * 2)
    return res 

# Llamada a la función doble_lista con el parámetro [1, 4, 3]
doble_lista([1, 4, 3])

# Definición de la funcion doble_lista mediante comprensión.
def doble_lista_compr(lista):
    res = [lista[i] * 2 for i in range(len(lista))]
    return res

# Llamada a la función doble_lista mediante comprensión con el parámetro [1, 4, 3]
doble_lista_compr([1, 4, 3])

# Definición de la funcion aplica, que recibe los siguientes parámetros:
#   - Una lista
#   - Una función (por defecto tomará el valor doble)
# La función aplica devuelve una lista en la que se ha aplicado la funcion a cada elemento de la lista original 
def aplica(lista, func=doble):
    res = []
    for i in lista:
        res.append(func(i))
    return res

# Llamada a la función aplica con los parámetros [1, 4, 3] y doble
aplica([1, 4, 3], doble)

# Llamada a la función aplica usando la función por defecto doble
aplica([1, 4, 3])

# Definición de la función triple, que devuelve el parámetro recibido multiplicado por 3 
def triple(x):
    return x*3

# Llamada a la función aplica con los parámetros [1, 4, 3] y triple
aplica([1, 4, 3], triple)

# Llamada a la función aplica con los parámetros:
#   - [1, 4, 3]
#   - una función lambda que multiplique el parámetro recibido por 3
aplica([1, 4, 3], lambda x: x*3)

# Creación la variable tupla, asignándole una tupla con los valores 1 y 'b'
tupla = (1, 'b')

# Acceso al segundo componente de la variable tupla
tupla[1]

# Extracción de los componetes de tupla en las dos variables x e y
x=tupla[0]; y=tupla[1]
print(x, y)

# Creación la variable lista, asignándole una lista con los valores 10, 20, 30 y 'a'
lista = [10, 20, 30, 'a']

# Cálculo de la longitud de lista
len(lista)

# Acceso a los siguentes componentes de la variable lista:
# - Primer elemento
# - Lista con el segundo y tercer elemento
# - Lista con todos los elementos menos el primero
# - Lista con los tres primeros elementos
# - Último elemento
print(lista[0])
print(lista[1:3])
print(lista[1:])
print(lista[-1])

#  Creación la variable lista_tuplas, con los elementos (1, 'a') y (2, 'b')
lista_tuplas = [(1, 'a'), (2, 'b')]

# Recorrido por comprensión de la variabe lista_tuplas dando como resultado ['1a', '2b']
[str(i) + str(j) for (i,j) in lista_tuplas]

# Creación de un rango de valores de 0 a 9
range(10)

# Creación de una lista a partir de un rango de valores de 0 a 9
[i for i in range(10)]

# Creación, por comprensión, de una lista de números pares multiplicando por 2 los valores de un rango de 0 a 9
[i*2 for i in range(10) if i % 2 == 0]

# Creación de la variable dicc que contiene un diccionario con las claves 'a' y 'b', y los respectivos valores 20 y 2
dicc = {'a':20, 'b':2}

# Acceso al valor asociado a la clave 'a' en dicc
dicc['a']

# Eliminación de la entrada en dicc correspondiente a la clave 'b'
dicc.pop('b')
print(dicc)

# Creación de una entrada en dicc con la clave 'c' y el valor 10
dicc.update({'c':10})
print(dicc)

# Intento de acceso a la clave inexistente 'd' en dicc
# dicc['d']

# Acceso seguro a la clave inexistente 'd' en dicc mediante el método get
dicc.get('d')
print(dicc)

# Acceso iterativo a todos los elementos de dicc
for i in dicc.keys():
    print(i)

print('###################')

for j in dicc.values():
    print(j)
    
print('###################')

for t in dicc:
    print(t)

# Creación de un diccionario por comprensión:
#  - Las claves son los números del 0 al 5
#  - Los valores son el doble de cada clave
{i:i*2 for i in range(6)}

# FIN