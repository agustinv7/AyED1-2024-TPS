def crear_diccionario(n: int) -> dict:
    keys = list(i+1 for i in range(12))
    valores = list(i*n for i in keys)
    diccionario = (dict(zip(keys, valores)))
    return diccionario

n = int(input("Ingrese un numero: "))


crear_diccionario(n)