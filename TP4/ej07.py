"""
Escribir  una  función  para  eliminar  una  subcadena  de  una  cadena  de  caracteres,  a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-
tante. Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanada
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


def subcadena_con_rebandas(cadena: str, posicion: int, cantidad: int) -> str:
    """

    Args:
        cadena (str): recibo una frase
        posicion (int): recibo la posicion desde donde quiero eliminar
        cantidad (int): recibo cuantos caracteres quiero eliminar

    Returns:
        str: retorno la cadena final
    """
    return cadena[:posicion] + cadena[posicion + cantidad :]


def subcadena_sin_rebandas(cadena: str, posicion: int, cantidad: int) -> str:
    pass


def menu():
    opciones = ["Subcadena con rebandas", "Subcadena sin rebandas", "Salir"]
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
                    frase = subcadena_sin_rebandas(cadena, posicion, cantidad)
                    print(frase)
                case 3:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion no valida. \n")
    else:
        print("Numero inválido")


if __name__ == "__main__":
    menu()
