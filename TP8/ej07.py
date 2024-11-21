def eliminando_numeros(conjunto:set) -> None:
    numeros_eliminados = 0
    while True:
        try:
            numero_a_eliminar = int(input("Ingrese un numero a eliminar: "))
            if numero_a_eliminar == -1:
                print("Saliendo...")
                break
            if numeros_eliminados == 9:
                print("Ha eliminado todos los numeros")
                break
            if numero_a_eliminar in conjunto:
                conjunto.remove(numero_a_eliminar)
                numeros_eliminados += 1
                print(conjunto)
        except IndexError:
            print("Ingrese nuevamente un numero")
    return None

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9}
eliminando_numeros(conjunto)