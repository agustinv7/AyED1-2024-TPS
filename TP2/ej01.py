"""
Desarrollar  cada  una  de  las  siguientes  funciones  y  escribir  un  programa  que  per-
mita verificar su  funcionamiento imprimiendo la lista luego de invocar  a cada fun-
ción:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen-
tos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar 
se  ingresa  desde  el  teclado  y  la  función  lo  recibe  como  parámetro.  No  utilizar 
listas auxiliares.
d. Determinar  si  el  contenido  de  una  lista  cualquiera  es  capicúa,  sin  usar  listas 
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]
"""

import random as rn


def carga_al_azar(lista: list, cantidad: int) -> list:
    """
    Esta funcion recibe como parámetros una lista vacia y un numero entero
    La lista se irá cargando a medida que se itera en el for
    El numero entero indica la cantidad de veces que se iterará el for
    Luego appendeo los números cargados al azar en la lista
    Retorno una lista
    """
    for _ in range(cantidad):
        numeros = rn.randint(1000, 9999)
        lista.append(numeros)
    return lista


def producto(lista: list) -> int:
    """
    El parámetro que recibe esta funcion es la lista cargada anteriormente
    Esta funcion itera por los elementos que hay en la lista y devuelve el
    producto total de los elementos
    Retorna el producto final
    """
    producto = 1
    # declaro la variable producto en 1 para poder multiplicar el valor de i
    for i in lista:
        producto *= i
        # a medida que recorre la lista, se guarda el valor en producto
        # para multiplicar el resultado por el siguiente valor
    return producto


def eliminar_numero(lista: list, numero_a_eliminar: int) -> list:
    """
    Recibimos como parametro una lista cargada y un numero entero a eliminar
    El numero entero a eliminar debe ser de 4 cifras y se carga a mano
    La funcion hace una copia de la lista principal y busca si existe el numero
    a eliminar en la copia.
    Si el numero está o no, se retorna la copia de la lista
    """
    copia_lista = lista.copy()
    # copio la lista principal para no modificar los datos iniciales
    for i in copia_lista:
        # recorro los elementos de la copia
        if numero_a_eliminar == i:
            # si el numero a eliminar coincide con un elemento de la lista
            copia_lista.remove(i)
            # elimino el elemento
    return copia_lista


def es_capicua(lista: list) -> bool:
    """
    Recibo como parámetro la lista principal para verificar si es capicua
    Retorna un booleano
    """
    for i in range(len(lista) // 2):
        # recorro hasta la mitad de la longitud de la lista
        if lista[i] != lista[-1 - i]:
            # si el primer indice de la lista, es distinto al último elemento - posicion i
            # retorna falso
            return False
        # si no retorna falso, entonces la lista es capicua, retorna true
    return True


lista = []
cantidad = rn.randint(10, 99)
numero_a_eliminar = int(input("Ingrese un numero a eliminar de 4 cifras: "))
print(cantidad)
print(carga_al_azar(lista, cantidad))
print(producto(lista))
print(eliminar_numero(lista, numero_a_eliminar))
