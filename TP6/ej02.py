import os

longitud = int(input("Ingrese el tamaño del archivo: "))
contenido = 0


while True:
    try:
        with open("c:/Users/Usuario/Desktop/nombres/nombres.txt", "rt", encoding="utf-8-sig") as archivo:
            for i in archivo:
                print(len(i.encode("utf-8")))
    except Exception as e:
        print("Error {e}")
        #print(archivo.read(longitud))

#with open("c:/Users/Usuario/Desktop/nombres/nombres_01.txt", "wt", encoding="utf-8") as archivo_01:
#    archivo_01.write(contenido)
 