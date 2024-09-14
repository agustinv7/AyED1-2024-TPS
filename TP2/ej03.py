"""
Crear  una  lista  con  los  cuadrados  de  los  números  entre  1  y  N  (ambos  incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valo-
res de la lista.
"""


def crear_lista(n: int, lista: list) -> list:
    """
    Reciben como parámetros n que es un numero entero y una lista vacia
    Se retorna la lista cargada con datos
    """
    for i in range(1, n + 1):
        resultado = i**2
        lista.append(resultado)
    return lista


def ultimos_10_valores(lista: list) -> list:
    """
    Esta funcion recibe una lista como parametro y guarda en una lista los ultimos 10 valores
    """
    valores = lista[-10:]
    return valores


def menu():
    opciones = [
        "Generar una lista con los cuadrados entre 1 y N",
        "Imprimir los ultimos 10 valores de la lista",
        "Salir",
    ]
    lista = []
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                n = int(input("Ingrese un numero mayor a 0: "))
                lista = crear_lista(n, lista)
                print(f"La lista con los elementos es \n{lista}")
                print()
            case 2:
                ultimos_valores = ultimos_10_valores(lista)
                print(f"Los ultimos 10 valores de la lista son \n:{ultimos_valores}")
                print()
            case 3:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")


if __name__ == "__main__":
    menu()