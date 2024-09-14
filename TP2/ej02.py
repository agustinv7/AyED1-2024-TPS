# Uso diccionarios dentro de listas
ciudades = [{"cp":1425, "nombre":"CABA"},
 {"cp":1900, "nombre":"La Plata"}]

print(f"Código postal La Plata: {ciudades[1]['cp']}\n")

#Agregar un elemento
ciudades.append({"cp":1878, "nombre":"Quilmes"})

#Podemos recorrer por objeto
for ciudad in ciudades:
    print(f"{ciudad['nombre']:<10} {ciudad['cp']}")