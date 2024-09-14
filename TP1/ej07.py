"""
Escribir  una  función  diasiguiente(dia,  mes  año)  que  reciba  como  parámetro  una 
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
ni agregados, desarrollar programas que permitan:

a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
 
"""


def diasiguiente(dia: int, mes: int, anio: int) -> tuple:
    """
    Dia tiene que corresponder a un numero entero
    Mes tiene que corresponder a un numero entero
    Año tiene que corresponder a un numero entero
    Retorna una tupla con la fecha
    """

    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # declaro los meses en una lista

    if anio in anios_bisiestos:
        dias_mes[1] = 29
    # si anio está en la tupla con los anios biciestos correspondientes, febrero pasa a tener 29 dias
    dia += 1
    # sumo un día por el enunciado
    if dia > dias_mes[mes - 1]:
        # si día es mayor al valor del mes indicado
        dia = 1
        # día es el primer día del mes
        mes += 1
    # sigue al siguiente mes
    if mes > 12:
        # si mes es mayor a diciembre
        anio += 1
    # se le suma un año
    fecha = (dia, mes, anio)
    return fecha


# a. Sumar N días a una fecha
def suma_dias(dia: int, mes: int, anio: int, n: int) -> tuple:
    """
    Se ingresan datos enteros en el día, mes, anio y n
    La funciona retorna una tupla con la fecha actualizada
    """
    for _ in range(n):
        # recorro el rango de N y uso el _ para ignorar el valor del iterador porque no lo voy a usar
        dia, mes, anio = diasiguiente(dia, mes, anio)
        # a los parámetros que ingreso, utilizo la funcion diasiguiente para sumarle 1 a la fecha
    fecha_actualizada = (dia, mes, anio)
    return (
        fecha_actualizada  # retorno en una tupla la fecha actualizada sumandole n dias
    )


# b Calcular la cantidad de días existentes entre dos fechas cualquiera.
def diferencia_entre_fechas(
    dia1: int, mes1: int, anio1: int, dia2: int, mes2: int, anio2: int
) -> int:
    """
    Se ingresan 2 fechas, todos los numeros deben ser enteros. dia2, mes2, y anio2 tiene que ser una fecha
    mayor a dia1, mes1, anio1
    retorna contador que es la diferencia que hay entre las fechas
    """
    contador = 0
    # este contador se utilizará para ver la diferencia entre dias
    while (dia2, mes2, anio2) > (dia1, mes1, anio1):
        # utilizo un while para recorrer las veces que sean necesarias siempre y cuando la segunda
        # fecha sea mayor a la primera
        dia1, mes1, anio1 = diasiguiente(dia1, mes1, anio1)
        # para la menor fecha, utilizo la función diasiguiente para disminuir la diferencia entre las 2 fechas
        contador += 1
        # le añado 1 por cada vez que itere
    # el while finaliza cuando no hay diferencias entre ambas fechas
    if contador > 0:
        # si la diferencia entre las fechas es mayor a 0
        return contador
        # se retorna el contador
    return contador


anios_bisiestos = tuple(range(1584, 2100, 4))
print(diasiguiente(29, 2, 2024))

# A
n = 5
dia, mes, anio = 10, 5, 2022
nuevo_dia, nuevo_mes, nuevo_anio = suma_dias(10, 5, 2022, 5)
nueva_fecha = nuevo_dia, nuevo_mes, nuevo_anio
print(f"La nueva fecha es {nueva_fecha}")


# B
dia1, mes1, anio1 = 12, 8, 2012
dia2, mes2, anio2 = 20, 8, 2012
diferencia_final = diferencia_entre_fechas(dia1, mes1, anio1, dia2, mes2, anio2)
print(
    f"La diferencia de dias entre {dia1, mes1, anio1} y {dia2, mes2, anio2} es de {diferencia_final} dias."
)
