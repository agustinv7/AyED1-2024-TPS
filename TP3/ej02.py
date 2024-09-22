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
        bool: retorna true si se cumple la condicion si es natural, caso contrario, false
    """
    if n > 0:
        return True
    return False


def crear_matriz(n: int) -> list:
    """
    Args:
        n (int): recibe como parametro un numero entero para crear la matriz de N x N

    Returns:
        None: retorna None
    """
    while True:
        if verificar_n(n):
            matriz = [[0 for _ in range(n)] for _ in range(n)]
            # genero una lista con el elemento 0 n cantidad de veces
            return matriz
        else:
            print("Ingrese un numero mayor a  0: ")


# A
def funcion_a(n: int) -> list:
    """

    Args:
        n (int): recibe como parámetro N que es el tamaño que se utiliza para crear la matriz

    Returns:
        list: retorna la matriz con los datos modificados
    """
    matriz_a = crear_matriz(n)
    for i in range(n):
        # recorro la matriz
        matriz_a[i][i] = 1 + 2 * i
        # selecciono el valor correspondiente y le asigno un nuevo valor
    return matriz_a


# B
def funcion_b(n: int) -> list:
    """_summary_

    Args:
        n (int): recibe como parámetro N que es el tamaño que se utiliza para crear la matriz

    Returns:
        list: retorna la matriz con los datos modificados
    """
    matriz_b = crear_matriz(n)
    for i in range(n):
        # recorro la matriz
        matriz_b[i][-1 - i] = 3 ** (3 - i)
        # recorro toda las listas y cada vez que itera, lo hace por cada lista y cada elemento de la lista
        # la posicion [-1-i] es igual a  decir la ultima posicion menos el valor de i
        # modifico el valor final
    return matriz_b


# C
def funcion_c(n: int) -> list:
    """_summary_

    Args:
        n (int): recibe como parámetro N que es el tamaño que se utiliza para crear la matriz

    Returns:
        list: retorna la matriz con los datos modificados
    """
    matriz_c = crear_matriz(n)
    for i in range(n):
        for j in range(i + 1):
            # itero desde el elemento i+1, incrementando cada vez que vuelve a empezar el bucle
            matriz_c[i][j] = n - i
            # el valor asignado es el ingresado en pantalla - i
    return matriz_c


# D
def funcion_d(n: int) -> list:
    """

    Args:
        n (int): recibe como parámetro N que es el tamaño que se utiliza para crear la matriz

    Returns:
        list: retorna la matriz con los datos modificados
    """
    matriz_d = crear_matriz(n)
    inicio = 8
    for i in range(n):
        for j in range(n):
            matriz_d[i][j] = inicio
            # a toda la lista le ingreso el valor de inicio
        inicio //= 2
        # por cada iteracion en el primer for, a inicio le reasigno el valor
    return matriz_d


# E
def funcion_e(n: int) -> list:
    """

    Args:
        n (int): recibe como parámetro N que es el tamaño que se utiliza para crear la matriz

    Returns:
        list: retorna la matriz con los datos modificados
    """
    inicio = 1
    matriz_e = crear_matriz(n)
    longitud = len(matriz_e)
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 != 0:
                # verifico si la la fila es par y la columna es impar
                matriz_e[i][j] = inicio
                # modifico el valor
                inicio = inicio + 1
                # guardo y sumo 1 al valor anterior para que en la iteracion posterior
                # se agregue el numero correspondiente
            elif i % 2 != 0 and j % 2 == 0:
                # verifico si la fila es impar y la columna es par
                matriz_e[i][j] = inicio
                # modifico el valor
                inicio = inicio + 1
                # guardo y sumo 1 al valor anterior para que en la iteracion posterior
                # se agregue el numero correspondiente
    return matriz_e


# F
def funcion_f(n: int) -> list:
    """

    Args:
        n (int): recibe como parámetro N que es el tamaño que se utiliza para crear la matriz

    Returns:
        list: retorna la matriz con los datos modificados
    """
    matriz_f = crear_matriz(n)
    inicio = 1
    for i in range(n):
        for j in range(i + 1):
            matriz_f[i][-1 + j] = inicio + i + j
            # tomo el ultimo indice y le resto la posicion de j en cada iteracion
            # le asigno el valor de la suma de inicio mas las iteraciones correspondientes
        inicio = inicio + j
        # por cada iteracion en el primer for, reasigno la variable inicio y le sumo j
    return matriz_f


# G
def funcion_g():
    pass


# H
def funcion_h():
    pass


# I
def funcion_i():
    pass


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
        while True:
            for i, opcion in enumerate(opciones):
                print(f"{i+1} - {opcion}")
            ingresar_opcion = int(input("Ingrese su opcion: "))
            match ingresar_opcion:
                case 1:
                    print(funcion_a(n))
                case 2:
                    print(funcion_b(n))
                case 3:
                    print(funcion_c(n))
                case 4:
                    print(funcion_d(n))
                case 5:
                    print(funcion_e(n))
                case 6:
                    print(funcion_f(n))
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
