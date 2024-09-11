"""
Escribir  una  función  diasiguiente(dia,  mes  año)  que  reciba  como  parámetro  una 
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
ni agregados, desarrollar programas que permitan:

a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
 
"""

def diasiguiente(dia:int, mes:int, anio:int):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #declaro los meses en una lista
    
    if anio in anios_bisiestos:
        dias_mes[1] = 29
    #si anio está en la tupla con los anios biciestos correspondientes, febrero pasa a tener 29 dias

    dia +=1
    #sumo un día por el enunciado
    
    if dia > dias_mes[mes -1]:
    #si día es mayor al valor del mes indicado
        dia = 1
    #día es el primer día del mes
        mes +=1
    #sigue al siguiente mes
    
    if mes > 12:
    #si mes es mayor a diciembre
        anio +=1
    #se le suma un año
        
    fecha = (dia, mes, anio)
    
    return fecha
    
    
anios_bisiestos = tuple(range(1584, 2100, 4))


print(diasiguiente(29, 2, 2024))