def eliminar_claves(nuevo_diccionario:dict, diccionario:dict, lista: list):
    claves_eliminadas = 0
    for key, value in diccionario.items():
        if key in lista:
            claves_eliminadas += 1
            nuevo_diccionario[key] = value
    return nuevo_diccionario, claves_eliminadas


diccionario = {300: "Matematica",
            200: "Educacion fisica",
            500: "Programacion"}

lista = [200, 300, 600]
nuevo_diccionaro, claves = eliminar_claves(diccionario, lista)
#falta corregir linea 17, se muestra el diccionario con los elementos borrados
print(f"El diccionario queda de la siguiente manera{nuevo_diccionaro}")
if claves == 1:
    print(f"Se elimino una clave")
elif claves >1 :
    print(f"La cantidad de claves eliminadas son {claves}")