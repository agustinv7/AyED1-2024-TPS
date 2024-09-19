"""
Leer  una  cadena  de  caracteres  e  imprimirla  centrada  en  pantalla.  Suponer  que  la 
misma tiene 80 columnas
"""

def centrar_cadena(cadena:str) -> str:
    """
    Esta funcion recibe una cadena como parametro. En ella se calcula como quedará en el centro de
    la pantalla
    Retorna la palabra centrada
    """
    ancho = 80
    longitud = len(cadena)
    espacios = (ancho - longitud) // 2
    centrada = '|' * espacios + cadena + espacios * '|'
    return centrada


def menu():
    opciones = [
        "Cadena centrada",
        "Salir"
    ]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                cadena = input("Ingrese una cadena: ")
                print(centrar_cadena(cadena))
            case 2:
                print("Saliendo ...")
                break
            case _:
                print("Ingrese una opcion valida")


if __name__ == "__main__":
    menu()
