keys = list(i+1 for i in range(20))
valores = list(i**2 for i in keys)

diccionario = dict(zip(keys, valores))

print(diccionario)