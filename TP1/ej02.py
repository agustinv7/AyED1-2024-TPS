"""
desarrollar una funcion que reciba tres numeros positivos, dia, mes y anio
y verificar si corresponde a una fecha válida
Debe tenerse en cuenta la cantidad de dias de cada mes incluyendo los bisiestos
Retornar True o False si la fecha es correcta o no
"""
#a la funcion le paso 3 parámetros correspondientes del dia mes y año
def verificar_fecha_valida(dia: int, mes: int, anio: int) -> int:
    if anio in anios_bisiestos:
        if (
            febrero(dia, mes, anio) 
            or meses_con_31_dias(dia, mes) 
            or meses_con_30_dias(dia, mes) == True
        ):
            return True
        else:
            return False
    elif anio in anios:
        if (
            febrero(dia, mes, anio) 
            or meses_con_31_dias(dia, mes) 
            or meses_con_30_dias(dia, mes) == True
        ):
            return True
        else:
            return False
    else:
        return False

                
def meses_con_31_dias(dia, mes):
    if dia in dias_31 and mes in meses_31:
        return True
    else:
        return False


def meses_con_30_dias(dia, mes):
    if dia in dias_30 and mes in meses_30:
        return True
    else:
        return False
    
    
def febrero(dia:int, mes:int, anio:int) -> bool:
    if anio in anios_bisiestos:
        if dia > 0 and dia < 30 and mes == 2:
            return True
        else:
            return False
    elif anio in anios:
        if dia > 0 and dia < 29 and mes == 2:
            return True
        else:
            return False
    else:
        return False
        

def menu():
    while True:
        print(verificar_fecha_valida(29, 2, 2009))
        break
    return None
    

dias_30 = tuple(range(1, 31))
dias_31 = tuple(range(1, 32))
meses_30 = (4, 6, 9, 11)
meses_31 = (1, 3, 5, 7, 8, 10, 12)
anios = tuple(range(1, 2200))
anios_bisiestos = tuple(range(1584, 2100, 4))


menu()