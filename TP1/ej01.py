"""
desarrollar una funcion que reciba 3 numeros enteros y devuelva el mayor de los 3
devolver -1 en caso de no haber ninguno.
desarrollar tambien un programa para ingresar los tres valores, invocar a la funcion
y mostrar el maximo hallado o un mensaje informativo si este no existe
"""

# esta funcion recibe 3 parámetros, dentro de la lista están los 3 numeros


def mayor_numero(a: int, b: int, c: int) -> None:
    lista = [a, b, c]
    lista.sort()
    # se ordenan todos los elementos con un sort de menor a mayor
    if lista[0] == lista[-1]:
        return f"Todos los numeros son iguales"
    # comparo el primer y ultimo elemento de la lista.
    # si son iguales significa que todos los elementos son el mismo numero
    elif lista[-1] == lista[-2]:
        return f"No hay mayor estricto"
    # si el ultimo elemento y ante ultimo elemento son iguales, no existe mayor estricto
    else:
        return f"El numero {lista[-1]} es  el mayor"
    # si no se cumple ninguna de las condiciones, el ultimo elemento de la lista es el mayor estricto


def menu():
    while True:
        print("Ingrese 1 para entrar o cualquier numero para salir")
        opciones = int(input("Ingrese una opcion: "))
        if opciones == 1:
            a = int(input("Ingrese un numero: "))
            b = int(input("Ingrese un numero: "))
            c = int(input("Ingrese un numero: "))
            print(mayor_numero(a, b, c))
        else:
            print("Saliendo...")
        break


menu()


print("Hola mariano francisco")