"""
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funcio-
nes que generen cada una de ellas sin intervención humana y escribir un programa 
que  las  invoque  e  imprima  por  pantalla.  El  tamaño  de  las  matrices  debe  estable-
cerse como N x N, donde N se ingresa a través del teclado
"""


def verificar_n(n: int) -> bool:
    """
    Args:
        n (int): recibe como parametro un número entero

    Returns:
        bool: retorna true si se cumple la condicion, caso contrario, false
    """
    if n > 0:
        return True
    return False


def crear_matriz(n: int) -> list:
    """
    Args:
        n (int): recibe como parametro un numero entero

    Returns:
        list: retorna una matriz con las filas y columnas correspondientes
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    # genero una secuencia de numeros desde 0 hasta n -1 en el primer for dentro de la lista
    # en el segundo for realizo lo mismo
    return matriz


# A
def funcion_a(matriz: list) -> list:
    """
    Args:
        matriz (list): recibe como parametro la matriz realizada

    Returns:
        list: retorna la matriz con los datos modificados
    """
    for i in range(len(matriz)):
        # recorro la matriz
        matriz[i][i] = 1 + 2 * i
        # selecciono el valor correspondiente y le asigno un nuevo valor
    return matriz


# B
def funcion_b(matriz: list, n:int) -> list:
    """

    Args:
        matriz (list): recibo la matriz con los datos en 0
        n (int): recibo este parametro para usarlo en una fórmula para cambiar el valor de una lista

    Returns:
        list: retorno la matriz con los datos actualizados
    """
    for i in range(len(matriz)):
        #recorro la matriz
        matriz[i][-1 - i] = 3 ** (n - i)
        #recorro toda las listas y cada vez que itera, lo hace por cada lista y cada elemento de la lista
        #la posicion [-1-i] es igual a  decir la ultima posicion menos el valor de i
        #modifico el valor final
    return matriz

#C
def funcion_c(matriz:list) -> list:
    """
    Args:
        matriz (list): recibe como parametro la matriz con datos en 0

    Returns:
        list: retorna la matriz con los datos actualizados
    """
    for i in range(len(matriz)):
        matriz[i][i] = 4-i
    return matriz
def menu():
    opciones = [
        "Funcion A",
        "Funcion B",
        "Funcion C",
        "Funcion D",
        "Funcion E",
        "Funcion F",
        "Funcion G",
        "Funcion H",
        "Funcion I",
        "Salir",
    ]
    n = int(input("Ingrese el tamaño de la matriz: "))
    if verificar_n(n):
        matriz = crear_matriz(n)
        while True:
            for i, opcion in enumerate(opciones):
                print(f"{i+1} - {opcion}")
            ingresar_opcion = int(input("Ingrese su opcion: "))
            match ingresar_opcion:
                case 1:
                    print(funcion_a(matriz))
                case 2:
                    print(funcion_b(matriz, n))
                case 3:
                    print(funcion_c(matriz))
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    pass
                case 9:
                    pass
                case 10:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion no valida. \n")
    else:
        print("Número inválido")


if __name__ == "__main__":
    menu()
