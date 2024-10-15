import random as rn


def buscar_numero() -> None:
    """En esta funcion pido al usuario que ingrese un numero y luego se verifica si cumple
    con las condiciones.
    Se le pide un numero hasta que encuentre el numero correspondiente
    Si ingresa valores que no sean numéricos, se le contará un intento y se tomará como error

    Returns:
        _type_: Retorna none
    """
    numero_random = rn.randint(1, 500)
    intentos = 1
    while True:
        try:
            numero = int(input("Ingrese su numero: "))
            if numero == numero_random:
                print("Numero encontrado!")
                if intentos == 1:
                    print(f"Al usuario le llevó {intentos} intento \n")
                else:
                    print(f"Al usuario le llevó {intentos} intentos \n")
                break
            elif numero < numero_random:
                print("El numero a encontrar es mas grande \n")
            elif numero > numero_random:
                print("El numero a encontrar es mas chico \n")
            intentos += 1
        except ValueError:
            print("Ingrese solo numeros \n")
            intentos += 1
    return None


buscar_numero()
