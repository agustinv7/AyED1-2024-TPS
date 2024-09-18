"""
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car-
ga. Se solicita:
a. Informar  para  cada  socio,  cuántas  veces  ingresó  al  club.  Cada  socio  debe 
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
ingresos.  Mostrar  los  registros  de  entrada  al  club  antes  y  después  de 
eliminarlo. Informar cuántos ingresos se eliminaron.
"""


def carga_de_datos(socios: dict) -> dict:
    """
    Esta funcion recibe una lista vacia y en base a que se van cumpliendo las condiciones,
    se cargan los datos en ella
    Se retorna la lista cargada con datos
    """
    while True:
        # utilizo while true para iterar las veces que desee el usuario
        legajo = int(input("Ingrese su legajo (-1 para salir): "))
        if legajo != -1:
            if validar_legajo(legajo) == True:
                # si el legajo es valido
                if legajo in socios:
                    # si el legajo está en el diccionario
                    socios[legajo] += 1
                    # le agrego 1 al valor
                else:
                    socios[legajo] = 1
                    # en el caso de que no esté cargado
                    # se agrega el legajo al diccionario iniciandolo con el valor 1 y la key con el legajo
            else:
                print("Legajo invalido")
        else:
            print("Saliendo...")
            break
    return socios


def ingreso_por_socio(socios: dict) -> None:
    """
    Esta funcion recibe como parametro el diccionario con los datos cargados
    Itera por la key y value del diccionario.
    Retorna none
    """
    for socio, veces in socios.items():
        # utilizamos items para imprimir en pantalla key y value del diccionarion
        print(f"Socio {socio} - ingresó {veces}")
    return None


def socio_de_baja(socios: dict) -> None:
    legajo = int(input("Ingrese su legajo: "))
    if legajo in socios:
        # si el legajo esta en el diccionario
        eliminado = socios.pop(legajo)
        # utilizo pop para eliminar la key del diccionario, da como resultado el value
        print(f"Se eliminaron {eliminado} ingresos del socio {legajo}")
    else:
        print("Ese legajo no está ingresado")
    return None


def validar_legajo(legajo):
    if legajo > 9999 and legajo < 100000:
        return True
    return False


def menu():
    opciones = ["Carga de datos", "Ingresos por socio", "Socios de baja", "Salir"]
    socios = {}
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                carga_de_datos(socios)
                print()
            case 2:
                ingreso_por_socio(socios)
            case 3:
                socio_de_baja(socios)
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")


if __name__ == "__main__":
    menu()
