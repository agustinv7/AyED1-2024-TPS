from math import sqrt


def obtener_raiz() -> float:
    """
    En esta funcion se le pide al usuario que ingrese un numero positivo para
    ver cual es la raiz cuadrada del mismo

    Returns:
        float: Retorna un numero flotante
    """
    while True:
        try:
            x = float(input("El numero elegido es: "))
            r = sqrt(x)
        except ValueError:
            print("Ingrese numeros positivos")
        else:
            resultado = round(r, 2)
            return resultado


print(obtener_raiz())
