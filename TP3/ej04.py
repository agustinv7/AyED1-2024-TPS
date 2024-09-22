"""
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna re-
presenta el día de la semana y cada fila a una de sus fábricas.

Se solicita:
a. Crear una matriz con datos generados al azar para N fábricas durante una 
semana,  considerando  que  la  capacidad  máxima  de  fabricación  es  de  150 
unidades  por  día  y  puede  suceder  que  en  ciertos  días  no  se  fabrique  nin-
guna. 
b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica. 
c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
por cada fábrica
"""

import random as rn


def verificar_n(n: int) -> bool:
    """
    Args:
        n (int): recibe como parametro un número entero

    Returns:
        bool: retorna true si se cumple la condicion si es natural, caso contrario, false
    """
    if n > 0:
        return True
    return False


def numeros_random() -> list:
    """

    Returns:
        list: retorna una lista del
    """
    numeros = list(set(i for i in range(151)))
    return numeros


# A
def datos_fabricas(matriz: int, n: int) -> list:
    """

    Args:
        matriz (int): La matriz se utiliza para cargar los datos de la produccion de bicicletas por fabrica
        n (int): Se carga un numero natural para verificar cuantas fabricas producen bicicletas

    Returns:
        list: retorna una matriz con los datos cargados
    """
    produccion = numeros_random()
    # genero una lista del 0 al 151 que son las unidades que puede producir la fabrica
    for i in range(n):
        produccion_fabrica_n = []
        # creo una lista vacia donde estaran los datos de produccion
        for j in range(6):
            # itero 6 veces, del lunes al sabado, del 0 al 5
            produccion_dia = rn.choice(produccion)
            # selecciono un numero random que es una produccion de un dia
            produccion_fabrica_n.append(produccion_dia)
            # appendeo a la produccion de la fabrica
        matriz.append(produccion_fabrica_n)
        # añado la lista a la matriz
    return matriz


# B
def produccion_total_fabrica(matriz: list) -> None:
    """

    Args:
        matriz (list): necesito la matriz con datos cargados para poder mostrar el total producido por fabrica

    Returns:
        list: None
    """
    if len(matriz) > 0:
        for i in range(len(matriz)):
            total = sum(matriz[i])
            print(f"El total de la fabrica {i+1} es de {total} bicicletas")
    print()
    return None


# C
def mayor_produccion_dia(matriz: list) -> list:
    """

    Args:
        matriz (list): recibo la lista cargada con datos

    Returns:
        list: retorno una lista con el primer indice como numero de fabrica y el segundo como cantidad producida
    """
    datos_mayor_produccion = []
    # en esta lista se guarda que fabrica produjo la mayor cantidad de bicicletas y tambien la cantidad
    mayor = 0
    fabrica = 0
    if len(matriz) > 0:
        # verifico si la matriz no esta vacia
        for i in range(len(matriz)):
            for j in range(6):
                if matriz[i][j] >= mayor:
                    # verifico si la cantidad de bicicletas producidas es mayor o igual que mayor
                    mayor = matriz[i][j]
                    # reasigno el valor de mayor
                    fabrica = i
                    # guardo que fabrica hizo esa produccion
        datos_mayor_produccion.append(fabrica)
        datos_mayor_produccion.append(mayor)
        # appendeo los datos a una lista al terminarse ambas iteraciones
        return datos_mayor_produccion
    else:
        print("No hay datos en la matriz")


# D
def dia_mas_productivo(matriz: int) -> tuple:
    total_dias = [sum(fabrica[i] for fabrica in matriz) for i in range(len(matriz[0]))]
    # en la primer iteracion, indica la cantidad de columnas que hay en la primer lista
    # en la segunda iteracion, accede al elemento i de cada columna y los suma
    # el valor queda guardado en la posicion j
    dia_productivo = total_dias.index(max(total_dias))
    # en esta variable, accedo al indice del dia de mayor produccion
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
    return dias[dia_productivo], total_dias[dia_productivo]


# E
def menor_cantidad_por_fabrica(matriz: list) -> None:
    menor_dia = [min(i) for i in matriz]
    return menor_dia


def menu():
    opciones = [
        "Crear los datos para las fábricas",
        "Mostrar el total de la produccion por fabrica",
        "Mostrar cual es la fabrica que mas produjo en un solo dia",
        "Mostrar el dia mas productivo",
        "Mostrar la menor cantidad fabricada por cada fabrica",
        "Salir",
    ]
    while True:
        matriz = []
        n = int(input("Ingrese cantidad de fabricas: "))
        if verificar_n(n):
            while True:
                for i, opcion in enumerate(opciones):
                    print(f"{i+1} - {opcion}")
                ingresar_opcion = int(input("Ingrese su opcion: "))
                print()
                match ingresar_opcion:
                    case 1:
                        produccion = datos_fabricas(matriz, n)
                        for i in range(len(produccion)):
                            print(f"La fabrica {i+1} produjo {produccion[i]}")
                        print()
                    case 2:
                        produccion_total_fabrica(matriz)
                    case 3:
                        fabrica, produccion = mayor_produccion_dia(matriz)
                        # guardo el dato de la fabrica y produccion en ambas variables
                        print(f"La fabrica {fabrica+1} produjo {produccion} bicicletas\n")
                        print()
                    case 4:
                        dia, total_produccion = dia_mas_productivo(matriz)
                        print(f"El dia {dia} con {total_produccion} bicicletas producidas, fue el dia mas productivo \n")
                        print()
                    case 5:
                        menos_produccion = menor_cantidad_por_fabrica(matriz)
                        for i, j in enumerate(menos_produccion):
                            print(f"La fábrica {i+1} fabricó {j} bicicletas")
                        print()
                    case 6:
                        print("Saliendo...")
                        break
                    case _:
                        print("Opcion no valida. \n")
        else:
            print("Numero inválido")


if __name__ == "__main__":
    menu()
