"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permi-
ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun-
ción:
a. Cargar  números  enteros  en  una  matriz  de  N  x  N,  ingresando  los  datos  desde 
teclado. 
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú-
mero se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
una lista con los números de las mismas
"""


# A
def crear_matriz(matriz: list) -> list:
    """
    Esta funcion recibe como parametro una matriz vacia y se va cargando a mano
    Retorna la matriz con los valores cargados
    """
    while True:
        n = int(input("Ingresar un numero (-1 para salir): "))
        x = int(input("Ingresar un numero (-1 para salir): "))
        y = int(input("Ingresar un numero (-1 para salir): "))
        if (n or x or y) == -1:
            print("Saliendo...")
            break
        else:
            matriz[0].append(n)
            matriz[1].append(x)
            matriz[2].append(y)
    return matriz


# C
def intercambiar_filas(matriz: list, posicion1: int, posicion2: int) -> list:
    """
    En esta matriz ingreso la matriz cargada, y 2 posiciones a intercambiar, en este caso filas
    Retorno la matriz modificada
    """
    matriz[posicion1], matriz[posicion2] = matriz[posicion1], matriz[posicion2]
    # declaro las variables con cada lista en la matriz e invierto su lugar
    return matriz


# D
def intercambiar_columnas(matriz: list, posicion1: int, posicion2: int) -> list:
    """
    En esta matriz ingreso la matriz cargada, y 2 posiciones a intercambiar, en este caso columnas
    Retorno la matriz modificada
    """
    for fila in matriz:
        # itero en cada lista de la matriz
        fila[posicion1], fila[posicion2] = fila[posicion2], fila[posicion1]
        # intercambio de posiciones en base a los parametros recibidos
    return matriz


# E
def trasponer_matriz(matriz: list) -> list:
    """
    Recibe como parámetro la matriz cargada
    El proposito en esta funcion es pasar los valores de las listas a filas si es que están en columnas
    y pasar a columnas si es que están en filas
    Retorna la matriz
    """
    if verificacion_matriz_cuadrada(matriz):
        # en esta funcion verifico si la matriz es cuadrada, si es así, ingreso al for
        for i in range(len(matriz)):
            for j in range(i + 1, len(matriz)):
                # en esta segunda iteracion, verifico que i != j
                matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
                # aca invoco a estos dos indices y intercambio sus posiciones entre si
        return matriz


# F
def calcular_promedio(matriz: list, n: int) -> str:
    """
    Esta funcion recibe como parámetro la matriz cargada con datos
    También recibe como parámetro n, que indica a que fila se le quiere calcular el promedio
    Retorna la matriz
    """
    if n < 0 and n > len(matriz):
        return "Matriz fuera de rango"
    fila = matriz[n]
    promedio = sum(fila) / len(fila) if len(matriz) > 0 else 0
    # el promedio es la suma de todos los elementos de la lista / el largo de la lista
    # si la matriz es mayor a 0, se puede cumplir el calculo del promedio, caso contrario, devuelve 0
    return f"El promedio de la fila {fila} es {promedio}"


# G
def calcular_porcentaje_por_fila(matriz: list, m: int) -> float:
    """
    Esta funcion recibe como parámetro la matriz cargada con datos
    También recibe como parametro n, que indica a que columna se le quiere calcular el porcentaje con valor impar
    Retorna el porcentaje
    """
    total_impares = 0
    total_numeros = 0
    if n >= 0 and n <= len(matriz):
        # si el numero ingresado por teclado cumple con esta condicion, ingreso al for
        for i in range(len(matriz)):
            total_numeros += 1
            if matriz[i][m] % 2 != 0:
                # si el valor de la matriz
                total_impares += 1
        porcentaje = (total_impares * 100) / total_numeros if total_numeros > 0 else 0
        # calculo el porcentaje multiplicando el total de impares * 100 y dividiendo ese resultado por el total de los numeros
    return porcentaje


# H
def simetrica_diagonal_principal(matriz: list) -> bool:
    if verificacion_matriz_cuadrada(matriz) == False:
        return False
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            # esta iteracion verifica que i != j
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


# i
def simetrica_diagonal_secundaria(matriz) -> None:
    copia_matriz = matriz.copy()
    # copio
    trasponer_matriz(copia_matriz)
    if simetrica_diagonal_principal(copia_matriz) == True:
        print("La diagonal secundaria de la matriz es simetrica")
    else:
        print("La diagonal secundaria de la matriz no es simetrica")
    return None


# j


def verificacion_matriz_cuadrada(matriz: list) -> bool:
    """
    En esta funcion, verifico si la matriz es cuadrada, es decir, que
    las filas y columnas de la matriz tienen la misma cantidad de elementos
    Retorno true si es cuadrada, false si no lo es
    """
    if len(matriz) == 0:
        # la matriz al no tener datos, es cuadrada
        return True
    numero_filas = len(matriz)
    # guardo el largo de la matriz
    numero_columnas = len(matriz[0])
    # guardo la longitud de la primera lista en la matriz
    if numero_filas != numero_columnas:
        # si el largo de la matriz no coincide con el largo de la primera lista
        return False
        # entonces la matriz no es cuadrada
    for fila in matriz:
        # itero por cada lista en la matriz
        if len(fila) == numero_columnas:
            # si el largo de cada lista de la matriz es igual al largo de la primera lista de la matriz
            return True
            # la matriz es cuadrada
    return False


def menu():
    opciones = [
        "Cargar numeros enteros en una matriz",
        "Ordenar de forma ascendente cada fila",
        "Intercambiar dos filas",
        "Intercambiar dos columnas",
        "Trasponer la matriz sobre si misma",
        "Calcular el promedio de los elementos de una fila",
        "Calcular el porcentaje de elementos con valor impar",
        "Determinar si la matriz es simetrica con respecto a su diagonal principal",
        "Determinar si la matriz es simetrica con respecto a su diagonal secundaria",
        "Determinar que columnas de la matriz son palíndromos",
        "Salir",
    ]
    matriz = [[], [], []]
    print("Las opciones son 0, 1, o 2")
    posicion_1 = int(input("Ingrese la primer posicion: "))
    posicion_2 = int(input("Ingrese la primer posicion: "))
    print("Las opciones son 0, 1, o 2")
    posicion1 = int(input("Ingrese la primer posicion: "))
    posicion2 = int(input("Ingrese la primer posicion: "))
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                crear_matriz(matriz)
                print()
            case 2:
                ordenar_matriz = [sorted(fila) for fila in matriz]
                print(f"{matriz} \n")
                # utilizo lista por comprension para ordenar de forma ascendente las filas de la matriz
                # utilizo la funcion sorted, ordena cada lista por cada iteracion.
            case 3:
                print(intercambiar_filas(matriz, posicion_1, posicion_2))
                print()
            case 4:
                print(intercambiar_columnas(matriz, posicion1, posicion2))
                print()
            case 5:
                print(trasponer_matriz(matriz))
            case 6:
                n = int(input("Ingrese un numero entre 0 y 2"))
                print(calcular_promedio(matriz, n))
            case 7:
                m = int(input("Ingrese un numero entre 0 y 2"))
                print(calcular_porcentaje_por_fila(matriz, m))
            case 8:
                print(simetrica_diagonal_principal(matriz))
            case 9:
                simetrica_diagonal_secundaria(matriz)
            case 10:
                # palindromo
                pass
            case 11:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")


if __name__ == "__main__":
    menu()
