"""
Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repi-
ta. Imprimir la matriz por pantalla.    
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


def numeros_random(n: int) -> list:
    """

    Args:
        n (int): recibo como parámetro un numero natural para crear una lista

    Returns:
        list: retorno la lista creada
    """
    numeros = list(set(i for i in range(n**2)))
    return numeros


def rellenar_matriz(n: int) -> list:
    matriz = []
    numeros = numeros_random(n)
    for i in range(n):
        fila = []
        # se van a crear n cantidad de listas
        for j in range(n):
            numero = rn.choice(numeros)
            # selecciono un numero a azar dentro de la lista numeros
            fila.append(numero)
            # appendeo el numero a la lista fila
            numeros.remove(numero)
            # elimino el numero de la lista de numeros
        matriz.append(fila)
        # termina toda la iteracion y appendeo la fila a la matriz
    return matriz


def menu():
    opciones = ["Lista random", "Salir"]
    n = int(input("Ingrese un numero mayor a 0: "))
    if verificar_n(n):
        while True:
            for i, opcion in enumerate(opciones):
                print(f"{i+1} - {opcion}")
            ingresar_opcion = int(input("Ingrese su opcion: "))
            match ingresar_opcion:
                case 1:
                    print(rellenar_matriz(n))
                case 2:
                    print("Salir")
                    break
                case _:
                    print("Opcion no valida. \n")
    else:
        print("Numero inválido")


if __name__ == "__main__":
    menu()
