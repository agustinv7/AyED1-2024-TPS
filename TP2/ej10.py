"""
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los 
elementos de la primera que sean impares. El proceso deberá realizarse utilizando 
la función filter(). Imprimir las dos listas por pantalla
"""

import random as rn


def menu():
    opciones = ["Lista random", "Lista con impares", "Salir"]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                lista_random = [rn.randint(1, 100) for _ in range(10)]
                # utilizo listas por comprension para crear una lista aleatoria
            case 2:
                lista_impares = list(filter(lambda x: x % 2 != 0, lista_random))
                # utilizo un constructor para crear una lista
                # utilizo filter para filtrar por los numeros que no son pares que recibe como parametro lambda
                # utilizo una funcion lambda para darle la condicion de que en cada iteracion, verifique si el numero es impar
                print(lista_random)
                print(lista_impares)
            case 3:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")


if __name__ == "__main__":
    menu()
