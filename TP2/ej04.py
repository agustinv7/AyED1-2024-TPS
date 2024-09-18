"""
Eliminar  de  una  lista  de  números  enteros  aquellos  valores  que  se  encuentren  en 
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista 
resultante. La función debe modificar la lista original sin crear una copia modificada
"""

import random as rn


def crear_lista(n: int, lista: list) -> list:
    """
    Recibe como parametro una lista
    Esta funcion crea una lista de 10 numeros aleatorios enteros entre 1 y 100
    Retorna la lista principal
    """
    for i in range(n):
        numeros = rn.randint(1, 10)
        lista.append(numeros)
    return lista


def numeros_a_eliminar(n: int, lista_eliminar: list) -> list:
    """
    Recibe como parametro una lista
    Esta funcion crea una lista de 10 numeros aleatorios enteros entre 1 y 100
    Retorna la lista con numeros a eliminar
    """
    for i in range(n):
        numeros = rn.randint(1, 10)
        lista_eliminar.append(numeros)
    return lista_eliminar


def menu():
    opciones = [
        "Crear lista",
        "Numeros a eliminar",
        "Salir",
    ]
    lista = []
    lista_eliminar = []
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                n = int(input("Ingrese un numero mayor a 0: "))
                lista = crear_lista(n, lista)
                print(lista)
                print()
            case 2:
                lista_eliminar = numeros_a_eliminar(n, lista_eliminar)
                lista_nueva = list(filter(lambda x: x not in lista_eliminar, lista))
                # uso filter para corroborar los elementos que hay en lista_eliminar y lista
                # si los elementos de lista no están en lista eliminar, entonces que los filtre
                # recibe como argumentos una funcion lambda y una lista
                print(lista_eliminar)
                print(lista_nueva)
                print()
            case 3:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")


if __name__ == "__main__":
    menu()
