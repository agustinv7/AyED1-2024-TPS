"""
Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que 
ingresa se anuncia en la recepción indicando su número de afiliado (número entero 
de  4  dígitos)  y  además  indica  si  viene  por  una  urgencia  (ingresando  un  0)  o  con 
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego 
se solicita:
a. Mostrar un listado de  los pacientes atendidos  por  urgencia y  un listado de 
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue 
atendido  por  turno  y  cuántas  por  urgencia.  Repetir  esta  búsqueda  hasta 
que se ingrese -1 como número de afiliado
"""


def carga_de_datos(lista_legajo: list, lista_estado: list) -> tuple:
    """
    Esta funcion recibe 2 listas vacias y en base a que se van cumpliendo las condiciones,
    se cargan los datos en ella
    Se retorna ambas listas
    """
    while True:
        # utilizo while true para iterar las veces que desee el usuario
        legajo = int(input("Ingrese su legajo (-1 para salir): "))
        if legajo != -1:
            if validar_legajo(legajo) == True:
                # si legajo es verdadero pido el siguiente dato
                estados_posibles()
                estado = int(input("Ingrese su estado: "))
                # pido el estado del paciente
                match estado:
                    # si el estado matchea con alguna de las opciones, se appendea a la lista
                    case 0:
                        lista_estado.append(estado)
                    case 1:
                        lista_estado.append(estado)
                    case 2:
                        print("Saliendo...")
                        break
                    case _:
                        print("Opcion no valida")
                    # sino se vuelve a pedir el dato
                lista_legajo.append(legajo)
                # una vez que salgo del match, appendeo el dato del legajo a la lista_legajo
                print("Carga exitosa \n")
            else:
                print("Legajo invalido")
        else:
            print("Saliendo...")
            break
    return lista_estado, lista_legajo


# A
def listados(lista_legajo: int, lista_estado: list) -> None:
    """
    En esta funcion se reciben las 2 listas cargadas y se retorna None
    En cada for recorremos el largo de una de las listas
    """
    print("Listado de pacientes por urgencia: \n")
    for i in range(len(lista_legajo)):
        # recorro la lista legajo
        if lista_estado[i] == 0:
            # si el indice de la lista estado es igual a 0
            print(f"El paciente {lista_legajo[i]} se atendió en la posicion {i+1}")
            # muestro en pantalla que el paciente con el legajo correspondiente, se atendio en la posicion i+1
            # le sumo 1 porque la posición inicial es de 0

    print("Listado de pacientes por turno: \n")
    for i in range(len(lista_legajo)):
        # recorro el indice de la lista legajo
        if lista_estado[i] == 1:
            # si el indice de la lista estado es igual a 1
            print(f"El paciente {lista_legajo[i]} se atendió en la posicion {i+1}")
            # muestro en pantalla que el paciente con el legajo correspondiente, se atendio en la posicion i+1
            # le sumo 1 porque la posición inicial es de 0
    return None


# B
def veces_atendido(lista_legajo: list, lista_estado: int, resultados: dict) -> dict:
    """
    En esta lista se ingresan las 2 listas con datos cargadas y también un diccionario vacio
    Se cargan datos en el diccionario en base a que se va iterando en ambas listas
    Retorna el diccionario
    """
    for legajo, estado in zip(lista_legajo, lista_estado):
        # itero en ambas listas por eso uso zip, de manera que tomo un elemento de cada lista
        if legajo not in resultados:
            # si el legajo no se encuentra en el diccionario
            resultados[legajo] = [0, 0]
            # creo en el diccionario resultados con la key legajo, una lista con dos valores iniciales en 0
        resultados[legajo][estado] += 1
        # en el diccionarion con la key correspondiente, sumo 1 según el estado del paciente
        # si es 0 lo sumo al primer valor, caso contrario, en el segundo valor
    return resultados


def validar_legajo(legajo):
    if legajo > 999 and legajo < 10000:
        return True
    return False


def validar_estado(estado):
    if estado == (0 or 1):
        return True
    return False


def estados_posibles():
    opciones = ["Urgencia", "Turno", "Salir"]
    for i, opcion in enumerate(opciones):
        print(f"{i} - {opcion}")
    return None


def menu():
    opciones = [
        "Carga de datos",
        "Listado de pacientes",
        "Veces atendido por pacientes",
        "Salir",
    ]
    lista_legajo = []
    lista_estado = []
    resultados = {}
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                carga_de_datos(lista_legajo, lista_estado)
                print()
            case 2:
                listados(lista_legajo, lista_estado)
                print()
            case 3:
                resultado = veces_atendido(lista_legajo, lista_estado, resultados)
                while True:
                    print(f"Esta es la lista de los pacientes {lista_legajo}")
                    afiliado = int(
                        input("Ingrese el número de afiliado (o -1 para salir): ")
                    )
                    if afiliado == -1:
                        break
                    if afiliado in resultado:
                        # si afiliado es alguna key en el diccionario, ingreso a la condicion
                        urgencias, turnos = resultado[afiliado]
                        # urgencias pertenece a las veces que el paciente fue por ese motivo al hospital
                        # turnos pertenece a las veces que el paciente fue por ese motivo
                        print(
                            f"El afiliado {afiliado} tuvo {urgencias} urgencias y {turnos} turnos."
                        )
                    else:
                        print(
                            f"No se encontraron registros para el afiliado {afiliado}."
                        )
                    print()
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Ingrese una opcion valida")


if __name__ == "__main__":
    menu()
