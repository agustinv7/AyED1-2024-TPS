def buscar_clave(diccionario:dict, buscado:str) -> list:
    lista = []
    for clave, valor_actual in diccionario.items():
        if valor_actual == buscado:
            lista.append(clave)
    return lista


diccionario = {"manzana": "roja", "banana": "amarilla", "uva": "morada", "limón": "amarilla"}
buscado = "amarilla"

print(buscar_clave(diccionario, buscado))