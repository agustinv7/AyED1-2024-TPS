"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres, 
indicando  la  posición  y  la  cantidad  de  caracteres  deseada.  Devolver  la  subcadena 
como  valor  de  retorno.  Escribir  también  un  programa  para  verificar  el  comporta-
miento  de  la  misma.  Ejemplo,  dada  la  cadena  "El  número  de  teléfono  es  4356-
7890"  extraer  la  subcadena  que  comienza  en  la  posición  25  y  tiene  9  caracteres, 
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si-
guientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
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


def subcadena_sin_rebandas(cadena: str, posicion: int, cantidad: int) -> str:
    """_summary_

    Args:
        cadena (str): recibo la frase
        posicion (int): se recibe la posicion desde donde quiero empezar a extraer
        cantidad (int): se recibe la cantidad de caracteres que quiero extraer

    Returns:
        str: _description_
    """
    return "".join(map(lambda i: cadena[i], range(posicion, posicion + cantidad)))
    # utilizo la funcion lambda para indicar que caracter quiero seleccionar
    # itero desde la posicion hasta la posicion+cantidad


def subcadena_con_rebandas(cadena: str, posicion: int, cantidad: int) -> str:
    """_summary_

    Args:
        cadena (str): _description_
        posicion (int): _description_
        cantidad (int): _description_

    Returns:
        str: _description_
    """
    return cadena[posicion : posicion + cantidad]


def menu():
    opciones = ["Subcadena sin rebandas", "Subcadena con rebandas", "Salir"]
    cadena = "Hoy independiente jugo horrible contra argentinos"
    posicion = 4
    cantidad = 13
    if verificar_n(posicion) and verificar_n(cantidad) and cadena != "":
        while True:
            for i, opcion in enumerate(opciones):
                print(f"{i+1} - {opcion}")
            ingresar_opcion = int(input("Ingrese su opcion: "))
            match ingresar_opcion:
                case 1:
                    print(subcadena_con_rebandas(cadena, posicion, cantidad))
                case 2:
                    print(subcadena_sin_rebandas(cadena, posicion, cantidad))
                case 3:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion no valida. \n")
    else:
        print("Numero inválido")


if __name__ == "__main__":
    menu()
