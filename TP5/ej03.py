"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes  cuyo  número  se  recibe  como  parámetro.  Los  nombres  de  los  meses  deberán 
obtenerse  de  una  lista  de  cadenas  de  caracteres  inicializada  dentro  de  la  función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones
"""


def ingresar_numero() -> int:
    """En esta funcion se verifica que el numero ingresado por el usuario
    sea mayor a 0

    Returns:
        int: Retorna el numero elegido
    """
    while True:
        try:
            numero = int(input("Ingrese el mes: "))
            if numero > 0:
                break
        except ValueError:
            print("Ingrese un numero positivo")
    return numero
    

def buscar_mes(mes: int) -> str:
    """_summary_

    Args:
        mes (int): Recibe como parametro un numero correspondiente al un mes del año

    Returns:
        str: Retorna el mes elegido o vacio si el numero no corresponde a un mes
    """
    lista_meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]
    while True:
        try:
            for _ in lista_meses:
                return lista_meses[mes-1]
        except IndexError:
            return ""
        

def menu():
    opciones = ["Buscar mes", "Salir"]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        try:
            ingresar_opcion = int(input("Ingrese su opcion: "))
            match ingresar_opcion:
                case 1:
                    numero = ingresar_numero()
                    print(buscar_mes(numero))
                case 2:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion no valida. \n")
        except ValueError:
            print("Ingrese una opcion valida")


if __name__ == "__main__":
    menu()
