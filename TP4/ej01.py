"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""

def cadena_capicua(cadena:str) -> bool:
    """
    Esta funcion recibe como parametro una cadena ingresada a mano
    Verifica si es capicua o no
    Retorna true si lo es, false si no lo es    
    """
    inicio = 0
    fin = len(cadena) -1
    #a fin le resto 1 para usar el indice en el while
    while inicio < fin:
        #utilizo un while para verificar si todos los 
        if cadena[inicio] != cadena[fin]:
            #si estos indices son iguales, se sigue iterando
            #caso contrario, se retorna falso
            return False
        inicio += 1
        #a inicio le sumo 1 para acercarse al medio de la cadena
        fin -= 1
        #a fin le resto 1 para acercarse al medio de la cadena
    return True
        
        
def comportamiento():
    cadena = anilina
    cadena_1 = hormiga
    assert (cadena_capicua(cadena)) == True
    assert (cadena_capicua(cadena_1)) == False
    return None
        
def menu():
    opciones = [
        "Cadena capicua",
        "Salir"
    ]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                cadena = input("Ingrese una cadena")
                print(cadena_capicua(cadena))
            case 2:
                print("Saliendo ...")
                break
            case _:
                print("Ingrese una opcion valida")


if __name__ == "__main__":
    menu()
