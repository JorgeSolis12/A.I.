class estrella(object):
opened = []
closed = []
#estados con los que estoy probando el algoritmo
q0 = {1:5, 2:4, 3:11}
q1 = {0:5, 3:6, 4:15}
q2 = {0:4, 3:5, 4:12}
q3 = {0:11, 1:6, 2:5, 4:5}
q4 = {1:15, 2:12, 3:5}
status = [q0,q1,q2,q3,q4]
distancia = 0

def destino(meta, entrada):
 
    actual = entrada
    global opened
 
    # Agregamos el status actual a la lista de estados abiertos
    opened.append(actual)
    finalized = False
 
    while not finalized:
 
        # Si el status actual es igual a la meta, entonces agregamos al status acual, a la lista de cerrados y devolvemos la lista la cual indica nuestro camino
        if actual == meta:
            closed.append(actual)
            return closed
        else:
            #lo agregamos a la lista de abiertos
            opened = [k for k in status[actual].keys() if k not in closed]
            # Cerramos el status actual
            closed.append(actual)
            # Ahora tomamos como status actual, aquel status vecino con el menor costo y distancia
            actual = menor_costo(actual, opened)
            # Limpiamos la lista de abiertos y realizamos una iteracion mas
            opened = []

# Funcion para determinar el status vecino con el menor costo y distancia
def menor_costo(actual, opened):
    # Obtenemos la suma del costo y la distancia menor, para un conjunto de estados vecinos 
    menor = min([status[actual][state] + distancia[state][meta] for state in opened])
    # Recorremos la lista de vecinos
    for state in opened:
        # devolvemos el menor de todos
        if status[actual][state] + distancia[state][meta] == menor:
            return state