"""
Desarrollar una función que reciba como parámetros dos números enteros positivos 
y  devuelva  como  valor  de  retorno  el  número  que  resulte  de  concatenar  ambos 
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per-
mite utilizar facilidades de Python no vistas en clase
"""


def concatenacion(a: int, b: int) -> int:
    primer = a
    segundo = b
    resultado = int(str(primer) + str(segundo))
    # en esta variable ingreso las variables previamente declaradas y las transformo a string
    # sumo ambas variables y las asigno a resultado
    return f"El resultado de la concatenacion de los numeros enteros es {resultado}"
    # retorno con f string el resultado


print(concatenacion(234, 456))
