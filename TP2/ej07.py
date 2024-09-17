"""
Intercalar los  elementos de  una lista entre los elementos de  otra.  La intercalación 
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] 
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden 
tener distintas longitudes.
"""


def intercalacion(lista1: list, lista2: list) -> list:
    longitud = min(len(lista1), len(lista2))
    # verifico el minino de ambas listas
    for i in range(longitud):
        # itero por la longitud de la menor lista
        lista1[2 * i + 1 : 2 * i + 1] = [lista2[i]]
        # en el indice de la lista i por cada iteracion
        # el indice que me da es justo el intermedio donde debe ir el elemento de la lista 2
    if len(lista2) > longitud:
        # si la lista 2 es mas larga que la primera
        lista1[len(lista1) :] = lista2[len(lista1) :]
        # luego del final de la lista 1, agrego todos los elementos que no se agregaron de la lista 2

    return lista1


def menu():
    opciones = [
        "Intercalacion",
        "Salir",
    ]
    lista1 = [5, 10, 15]
    lista2 = [20, 30, 40]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                n = int(input("Ingrese un numero mayor a 0: "))
                lista = intercalacion(lista1, lista2)
                print(lista)
                print()
            case 2:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")


if __name__ == "__main__":
    menu()
