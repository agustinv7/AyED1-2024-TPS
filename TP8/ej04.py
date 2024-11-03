import random as rn


def verificar_fichas(ficha_1:tuple, ficha_2:tuple) -> bool:
    """Recibo 2 tuplas para realizar la funcion
    Casteo las tuplas a set para utilizar el metodo .intersection

    Args:
        ficha_1 (tuple): Tupla con 2 numeros enteros entre 0 y 6
        ficha_2 (tuple): Tupla con 2 numeros enteros entre 0 y 6

    Returns:
        bool: Retorno True or False 
    """
    numeros = {0, 1, 2, 3, 4, 5, 6}
    set_1 = set(ficha_1)
    set_2 = set(ficha_2)
    return bool(numeros.intersection(set_1, set_2))


ficha_1 = (1, 2)
ficha_2 = (2, 3)
assert verificar_fichas((1,2), (3,4)) == False
assert verificar_fichas((1,2), (2,4)) == True