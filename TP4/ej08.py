"""
Desarrollar  una función que  devuelva una subcadena  con  los últimos N  caracteres 
de una cadena dada. La cadena y el valor de N se pasan como parámetros
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


def subcadena(cadena: str, n: int) -> str:
    return cadena[-n:]


def menu():
    opciones = ["Subcadena", "Salir"]
    n = int(input("Ingrese un numero mayor a 0: "))
    cadena = input("Ingrese una frase: ")
    if verificar_n(n) and cadena != "":
        while True:
            for i, opcion in enumerate(opciones):
                print(f"{i+1} - {opcion}")
            ingresar_opcion = int(input("Ingrese su opcion: "))
            match ingresar_opcion:
                case 1:
                    print(subcadena(cadena, n))
                case 2:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion no valida. \n")
    else:
        print("Numero inválido")


if __name__ == "__main__":
    menu()
