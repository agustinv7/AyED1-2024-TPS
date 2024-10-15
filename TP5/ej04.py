"""
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un  programa  para  imprimir  los  números  enteros  entre  1  y  100000,  y  que  solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl+C
"""


def imprimir_numeros() -> None:
    """En esta funcion imprimimos los numeros dentro del rango
    Utilizamos CTRC+C para interrumpir el programa.
    Usamos KeyboardInterrupt para que no genere error en la ejecucion del programa
    Preguntamos si desea continuar con la ejecucion del programa, que ingrese S
    Caso contrario, que ingrese N y se vuelve a ejecutar el programa

    Returns:
        _type_: Retorno None
    """
    while True:
        try:
            for i in range(100):
                print(i)
        except KeyboardInterrupt:
            print("Programa detenido")
        confirmacion = input("Desea continuar? S para seguir, N para salir\n")
        if confirmacion == "n":
            print("Programa terminado")
        else:
            print("Continuando")
            imprimir_numeros()
        return None


imprimir_numeros()
