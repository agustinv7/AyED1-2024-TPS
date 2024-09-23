"""
Escribir  una  función  filtrar_palabras()  que  reciba  una  cadena  de  caracteres  conte-
niendo una frase y un entero N, y devuelva otra cadena con las palabras que ten-
gan N  o más  caracteres  de  la cadena  original.  Escribir también un programa para 
verificar  el  comportamiento  de  la misma.  Hacer  tres  versiones  de  la  función, para 
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
"""


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


def filtar_palabras_a(cadena: str, n: int) -> str:
    palabras = cadena.split()
    # uso split para separar cada palabra y convertirla a cadena
    lista_palabras = []
    for i in palabras:
        if len(i) >= n:
            # compruebo si la longitud de cada cadena es mayor o igual a n
            lista_palabras.append(i)
            # appendeo la cadena a la lista
    return " ".join(lista_palabras)
    # utilizo join para ingresar un espacio a la frase final


def filtrar_palabras_b(cadena: str, n: int) -> str:
    return " ".join([i for i in cadena.split() if len(i) >= n])


def filtrar_palabras_c(cadena: str, n: int) -> str:
    return " ".join(filter(lambda i: len(i) >= n, cadena.split()))
    # utilizo lambda para verificar si se cumple esa condicion, pasandole como parametro, cada cadena creada con split
    # si se cumple, filtro las palabras correspondientes
    # por ultimo utilizo join para sumarle un espacio entre las cadenas


def menu():
    opciones = ["Ciclos normales", "Listas por comprension", "Funcion filter", "Salir"]
    n = int(input("Ingrese un numero mayor a 0: "))
    cadena = input("Ingrese una frase: ")
    if verificar_n(n) and cadena != "":
        while True:
            for i, opcion in enumerate(opciones):
                print(f"{i+1} - {opcion}")
            ingresar_opcion = int(input("Ingrese su opcion: "))
            match ingresar_opcion:
                case 1:
                    print(filtar_palabras_a(cadena, n))
                case 2:
                    print(filtrar_palabras_b(cadena, n))
                case 3:
                    print(filtrar_palabras_c(cadena, n))
                case 4:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion no valida. \n")
    else:
        print("Numero inválido")


if __name__ == "__main__":
    menu()
