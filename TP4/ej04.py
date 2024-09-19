"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y 
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En 
qué cambiaría la función si el rango de valores fuese diferente?
"""
def convertir_numero_romano(numero:int, valores_romanos:tuple) ->str:
    """
    En esta funcion se recibe un numero y una tupla con los valores de numeros romanos
    El proposito es transformar un numero entero a numeros romanos
    Se retorna un string mencionando el numero final o se retorna numero invalido
    """
    if verificar_numero(numero):
        resultado = ""
        for valor, simbolo in valores_romanos:
            #itero los valores y simbolos de la tupla de los numeros romanos
            while numero >= valor:
                #itero segun si el numero es mayor al valor de uno de los terminos de los numeros romanos
                resultado += simbolo
                #a la variable resultado le agrego el simbolo romano
                numero -= valor
                #al numero le resto el valor
        return f"El numero romano es {resultado}"
    return f"Ingrese un numero válido"
    
    
def verificar_numero(numero:int)->bool:
    if numero > 0 and numero < 4000:
        return True
    return False

def menu():
    opciones = [
        "Convertir un numero entero a numero romano",
        "Salir"
    ]
    valores_romanos = (
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    )
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                numero = int(input("Ingrese una clave numerica: "))
                print(f"El numero inicial es {numero}")
                print(convertir_numero_romano(numero, valores_romanos))
            case 2:
                print("Saliendo ...")
                break
            case _:
                print("Ingrese una opcion valida")


if __name__ == "__main__":
    menu()

