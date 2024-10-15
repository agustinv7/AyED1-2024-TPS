def generar_lista() -> list:
    """Esta funcion crea una lista de n elementos

    Returns:
        list: Retorno una lista
    """
    lista = []
    while True:
        try:
            n = int(input("Ingrese numeros (-1 para salir): "))
            if n != -1:
                lista.append(n)
            else:
                break
        except ValueError:
            print("Solo ingrese numeros")
    return lista


def buscar_posicion(lista: list) -> None:
    """Esta funcion busca un elemento dentro de una lista.

    Args:
        lista (list): Recibe una lista con datos

    Returns:
        _type_: Retorna None
    """
    posicion = 0
    intentos = 0
    if len(lista) > 0:
        while True:
            try:
                if intentos == 3:
                    print("Llego a los intentos maximos")
                    break
                print(lista)
                numero = int(input("Ingrese el numero a buscar: "))
                posicion = lista.index(numero)
                print(f"La posicion del numero {numero} es {posicion + 1}")
            except ValueError:
                print("Error")
                intentos += 1
                print(f"Intento {intentos}/3")
    return None


lista = generar_lista()
buscar_posicion(lista)
