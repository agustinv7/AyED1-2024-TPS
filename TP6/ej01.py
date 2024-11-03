separador = ";"
try:
    lista_terminaciones = ["Ian", "ini", "ez"]
    with open(
        "c:/Users/Usuario/Desktop/nombres/nombres.txt", "rt", encoding="utf-8"
    ) as arch:
        lineas = arch.readlines()
        for linea in lineas:
            nombre = linea.split(",")[0]
            if nombre[-len(lista_terminaciones[0]) : :] == "ian":
                try:
                    with open(
                        "c:/Users/Usuario/Desktop/nombres/ARMENIA.TXT",
                        "wt",
                        encoding="utf-8",
                    ) as arch_arm:
                        arch_arm.write(linea)
                except FileNotFoundError as msg:
                    print(f"No se encuentra el archivo: {msg}")
                except OSError as msg:
                    print(f"No se puede grabar el archivo: {msg}")
                except:
                    print("Error en los datos")
                else:
                    print(f"\nArchivo creado correctamente")
            elif nombre[-len(lista_terminaciones[1]) : :] == "ini":
                try:
                    with open(
                        "c:/Users/Usuario/Desktop/nombres/ITALIA.TXT",
                        "wt",
                        encoding="utf-8",
                    ) as arch_ita:
                        arch_ita.write(linea)
                except FileNotFoundError as msg:
                    print(f"No se encuentra el archivo: {msg}")
                except OSError as msg:
                    print(f"No se puede grabar el archivo: {msg}")
                except:
                    print("Error en los datos")
                else:
                    print(f"\nArchivo creado correctamente")
            elif nombre[-len(lista_terminaciones[2]) : :] == "ez":
                try:
                    with open(
                        "c:/Users/Usuario/Desktop/nombres/ESPAÑA.TXT",
                        "wt",
                        encoding="utf-8",
                    ) as arch_esp:
                        arch_esp.write(linea)
                except FileNotFoundError as msg:
                    print(f"No se encuentra el archivo: {msg}")
                except OSError as msg:
                    print(f"No se puede grabar el archivo: {msg}")
                except:
                    print("Error en los datos")
                else:
                    print(f"\nArchivo creado correctamente")
except FileNotFoundError as msg:
    print(f"No se encuentra el archivo: {msg}")
except OSError as msg:
    print(f"No se puede leer el archivo: {msg}")
except:
    print("Error en los datos")
else:
    print(f"\nArchivo leido correctamente")
