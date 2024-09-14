"""
Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa 
a través del teclado.
b. Recibir  una  lista  como  parámetro  y  devolver  True  si  la  misma  contiene  algún 
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos 
únicos de la lista original, sin importar el orden. 
Combinar estas tres funciones en un mismo programa
"""

import random as rn


def generar_lista(n: int, lista: list) -> list:
    """
    En esta funcion se reciben como parámetros para n un numero entero positivo y una lista vacia
    En ella se realiza la iteracion de N elementos y por cada iteracion, se agrega en la lista vacia
    un numero al azar entre 1 y 100
    Se retorna la lista cargada
    """
    for i in range(n):
        numero = rn.randint(1, 10)
        lista.append(numero)
    return lista


def elemento_repetido(lista: list) -> bool:
    """
    En esta funcion recibo como parametro una lista y se retorna un booleano
    En esta funcion, se iteran los elementos de la lista y si hay un dato repetido, retorna true
    caso contrario retorna falso
    """
    for elemento in set(lista):
        # uso set para buscar un dato repetido
        # itero cada elemento y utilizo set para buscar numeros repetidos
        if lista.count(elemento) > 1:
            # si el elemento está mas de una vez, es porque está repetido, retorno True
            return True
        # si esta condicion no se cumple, ningún numero se repite en la lista, retorno false
    return False


def elementos_unicos(lista: list, lista_nueva: list) -> list:
    """
    En esta funcion recibo dos listas, una cargada con datos y otra vacia.
    En esta funcion se iteran los elementos de la lista cargada y si un elemento es unico, es decir que no se repite
    se carga en una nueva lista
    Se retorna una tupla con esos datos
    """
    for elemento in set(lista):
        # usamos set para buscar un dato especifico
        if lista.count(elemento) == 1:
            # usamos count para ver si el elemento es igual a uno, si es asi, significa que es unico
            lista_nueva.append(elemento)
            # añado el elemento a la lista nueva
    return lista_nueva


def menu():
    opciones = [
        "Generar una lista de nombres aleatorios",
        "Ver si la lista tiene elementos repetidos",
        "Ver los elementos unicos de la lista",
        "Salir",
    ]
    lista = []
    lista_nueva = []
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                n = int(input("Ingrese un numero mayor a 0: "))
                lista = generar_lista(n, lista)
                print(f"La lista con los elementos es \n{lista}")
                print()
            case 2:
                if elemento_repetido(lista) == True:
                    print("Hay elementos que se repiten")
                else:
                    print("No se repiten elementos")
                print()
            case 3:
                if lista:
                    lista_unica = elementos_unicos(lista, lista_nueva)
                    print(f"{lista_unica}")
                else:
                    print("No hay elementos en la lista")
                print()
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")


if __name__ == "__main__":
    menu()
