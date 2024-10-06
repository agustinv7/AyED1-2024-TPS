"""
Realizar una  función que  reciba como  parámetros dos  cadenas  de  caracteres  con-
teniendo  números  reales,  sume  ambos  valores  y  devuelva  el  resultado  como  un 
número  real. Devolver -1  si alguna de las cadenas no contiene un número  válido, 
utilizando manejo de excepciones para detectar el error
"""


def sumar_cadenas(cadena_1: str, cadena_2: str) -> float:
    """Esta funcion suma ambas cadenas escritas por el usuario
    Se castean los datos tipo string a float y luego se realiza la suma correspondiente

    Args:
        cadena_1 (str): Se espera que se reciba un numero real
        cadena_2 (str): Se espera que se reciba un numero real

    Returns:
        float: Retorna la suma de ambas cadenas si el primer y segundo dato se pudo castear
        a flotante
        Caso contrario, se retorna -1.0
    """
    while True:
        try:
            primer_cadena = float(cadena_1)
            segunda_cadena = float(cadena_2)
        except ValueError:
            return float(-1)
        else:
            return primer_cadena + segunda_cadena


def menu():
    opciones = ["Sumar cadenas", "Salir"]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        try:
            ingresar_opcion = int(input("Ingrese su opcion: "))
            match ingresar_opcion:
                case 1:
                    cadena_1 = input("Ingrese numeros: ")
                    cadena_2 = input("Ingrese numeros: ")
                    print(sumar_cadenas(cadena_1, cadena_2))
                case 2:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion no valida. \n")
        except ValueError:
            print("Ingrese una opcion valida")


if __name__ == "__main__":
    menu()
