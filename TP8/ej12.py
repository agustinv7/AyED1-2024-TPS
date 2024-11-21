libreria = {300: "Matematica",
            200: "Educacion fisica",
            500: "Programacion"}


libreria_actualizada = {int (key * (1 + 15 / 100)): value for key, value in libreria.items()}

lista_precios = list(libreria_actualizada.keys())
precio_maximo = max(lista_precios)

for key, value in libreria_actualizada.items():
    if precio_maximo == key:
        print(f"El item {value} es el más costoso, vale {key}")
        
print(lista_precios)
