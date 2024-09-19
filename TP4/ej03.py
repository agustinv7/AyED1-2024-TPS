"""
Los números de claves de dos cajas fuertes están intercalados dentro de un número 
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa 
para obtener ambas claves, donde la primera se construye con los dígitos ubicados 
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en 
posiciones  pares.  Los  dígitos  se  numeran  desde  la  izquierda.  Ejemplo:  Si  clave 
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89
"""

def clave_maestra(clave:str) -> tuple:
    """
    La clave ingresada es un numero natural
    Retorna una tupla con ambas claves
    """
    clave_1 = ""
    clave_2 = ""
    if len(clave) > 0:
        #si la clave tiene mas de un caracter, ingreso al for
        for i in range(len(clave)):
            #itero por la longitud de la clave
            if i % 2 == 0:
                #si el indice de la clave es par
                clave_1 += clave[i]
                #a la variable clave_1 se le añade el caracter de clave[i]
            else:
                clave_2 += clave[i]
                #si es par
                #a la variable clave_2 se le añade el caracter de clave[i]
    return clave_1, clave_2
    
    
def menu():
    opciones = [
        "Ver claves maestras",
        "Salir"
    ]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                cadena = input("Ingrese una clave numerica: ")
                print(clave_maestra(cadena))
            case 2:
                print("Saliendo ...")
                break
            case _:
                print("Ingrese una opcion valida")


if __name__ == "__main__":
    menu()

