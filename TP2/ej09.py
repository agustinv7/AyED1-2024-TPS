"""
Generar  e  imprimir  una  lista  por  comprensión  entre  A  y  B  con  los  múltiplos  de  7 
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
"""

def lista_por_comprension(a, b) ->list:
    """
    Ingreso por teclado 2 numeros positivos distintos entre si
    retorno una lista por comprension
    """
    lista = [i for i in range(a, b) if i % 7 == 0 and i % 5 != 0]
    #itero en el rango de los parametros que recibo por teclado
    #si i es multiplo de 7 e i no es multiplo de 5, se suma a la lista
    return lista


def menu():
    opciones = [
        "Lista por comprension",
        "Salir",
    ]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                a = int(input("Ingrese un numero: "))
                b = int(input("Ingrese un numero: "))
                if a > b:
                    lista = lista_por_comprension(b, a)
                else:
                    lista = lista_por_comprension(a, b)
                print(lista)
                print()
            case 2:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")


if __name__ == "__main__":
    menu()
