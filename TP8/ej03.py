import re


def ingresar_mail() -> str:
    """Ingreso un dato, se espera un mail como hola@hola.edu.ar

    Returns:
        str: Retorna un input ingresado por el usuario
    """
    return input("Ingrese el mail: ")


def verificar_mail(expresion:str, mail:str) -> bool:
    """Se pide el mail a traves de un input, se verifica a traves de una expresion regular
    si es la esperada.


    Args:
        expresion (str): Paso como parametro la expresion regular a verificar
        mail_input (str): Ingreso un dato, se espera un mail


    Returns:
        bool: retorno true si se cumple o false si no
    """
    try:
        if re.fullmatch(expresion, mail):
            return True
        else:
            return False
    except (ValueError, KeyboardInterrupt) as e:
        print(f"\n{e}")


def separar_mail(expresion:str, mail_input:str) -> tuple:
    """Verifico si el mail es correcto, se separa los terminos, primero todos los caracteres
    antes del "@" y luego los caracteres antes de o delos "."

    Args:
        expresion (str): Paso como parametro la expresion regular a verificar
        mail_input (str): Ingreso un dato, se espera un mail

    Returns:
        tuple: Retorno una tupla con los datos si el mail es valido, caso contrario, una tupla vacia
    """
    mail_valido = verificar_mail(expresion, mail_input)
    if mail_valido:
        local, dominio = mail_input.split("@")
        return local, *dominio.split(".")
    return () 
    

def menu() -> None:
    opciones = ["Separar Mail en partes", "Salir"]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                expresion = r'^[a-zA-Z0-9]{4,}@[a-zA-Z0-9]{3,4}\.[a-zA-Z]{2,3}\.[a-zA-Z]{2}$'
                mail_input = ingresar_mail()
                print(separar_mail(expresion, mail_input))
            case 2:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")
        return None


if __name__ == "__main__":
    menu()
