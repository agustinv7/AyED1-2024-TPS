"""
Escribir una función que reciba una lista de números enteros como parámetro y la 
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro-
porciones relativas que cada elemento tiene en la lista original. Desarrollar también 
un  programa  que  permita  verificar  el  comportamiento  de  la  función.  Por  ejemplo, 
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""


def normalizar_lista(lista: list) -> list:
    """
    Esta funcion recibe una lista como parámetro y retorna una lista
    con los valores de la lista normalizados en una nueva lista
    """
    suma_total = sum(lista)
    # sumo todos los elementos de la lista
    normalizar = list(num / suma_total for num in lista)
    # utilizo un constructor de lista y dentro de el, a cada número de la lista lo divido
    # en cada iteración por la suma total
    return normalizar


def comportamiento():
    assert lista_ordenada([1, 2, 3, 4]) == [0.1, 0.2, 0.3, 0.4]
    assert lista_ordenada([2, 4, 6, 8]) == [0.1, 0.2, 0.3, 0.4]
    assert lista_ordenada([4, 8, 12]) == [0.4, 0.3, 0.2, 0.1]
    return None


def menu():
    opciones = [
        "Normalizar la lista",
        "Salir"
    ]
    lista = [16, 12, 8, 4]
    lista_eliminar = []
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                print(normalizar_lista(lista))
            case 2:
                print("Saliendo ...")
                break
            case _:
                print("Ingrese una opcion valida")


if __name__ == "__main__":
    menu()
