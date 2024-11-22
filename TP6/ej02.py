

def dividir_archivo(ruta:str, tamanio:int):
    try:
        with open(f"{ruta}", 'rt', encoding='utf-8')as archivo:
            contenido = archivo.read()
            tamanio_contenido = len(contenido)
            division = tamanio_contenido // tamanio
            contador = 0
            if tamanio > tamanio_contenido:
                raise("No se puede iterar, el contenido es menor a las particiones")
            for _ in range(division):
                texto = contenido[:tamanio]
                contenido = contenido[tamanio:]
                contador += 1
                archivo = f"parte{contador}.txt"
                with open(archivo, 'wt', encoding='utf-8') as arch_txt:
                    arch_txt.write(texto)
    except FileNotFoundError:
        print("Error: El archivo no existe.")
        exit()
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
        exit()
        
        
RUTA = 'C:/Users/Usuario/Documents/UADE/2DO CUATRIMESTRE 2024/2) Algoritmos y estructuras de datos/AyED1-2024-TPS/TP6/ARCHIVO_TXT/texto.txt'
tamanio = int(input("Ingrese el tamano de los archivos: "))

dividir_archivo(RUTA, tamanio)