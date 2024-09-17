"""
Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
está  ordenada  en  forma  ascendente  o  False  en  caso  contrario.  Por  ejemplo, 
ordenada([1,  2,  3])  retorna  True  y  ordenada(['b',  'a'])  retorna  False.  Desarrollar 
además un programa para verificar el comportamiento de la función.
"""

def lista_ordenada(lista:list) ->bool:
    """
    Esta funcion recibe como parámetro una lista de número, utilizo all y un for para iterar los
    elementos de la lista. Si se cumple la condicion, devuelvo True, caso contrario, False
    Retorno booleano
    """
    ascendente = all(lista[i] <= lista[i+1] for i in range(len(lista)-1))
    #con el metodo all, verifico si se cumple en todas las iteraciones, que i+1 es mayor a i
    #si se cumple, es porque la lista es ascendente, caso contrario, la lista es descendente
    return ascendente


def comportamiento():
    assert lista_ordenada([1, 2, 3, 4]) == True
    assert lista_ordenada(['a', 'b', 'c', 'd']) == True
    assert lista_ordenada([5, 4, 3, 2]) == False


if __name__ == "__main__":
    lista = [1, 2, 3, 4]
    lista_ordenada(lista)
    
    