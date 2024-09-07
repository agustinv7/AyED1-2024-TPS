"""
desarrollar una funcion que reciba tres numeros positivos, dia, mes y anio
y verificar si corresponde a una fecha válida
Debe tenerse en cuenta la cantidad de dias de cada mes incluyendo los bisiestos
Retornar True o False si la fecha es correcta o no
"""
#a la funcion le paso 3 parámetros correspondientes del dia mes y año
def verificar_fecha_valida(dia: int, mes: int, anio: int) -> int:
    if dia in dias and mes in meses: 
            if (meses_con_31_dias(dia, mes)) or (meses_con_30_dias(dia, mes)) or () == True:
                return True
    elif anio in anios:
        
            
def meses_con_31_dias(dia, mes):
    if dias == 31 and mes == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        return True
    else:
        return False


def meses_con_30_dias(dia, mes):
    if dias == 30 and mes == (4 or 6 or 9 or 11):
        return True
    else:
        return False
    
    
def febrero_biciesto(dia, mes):
    if dia > 0 and dia < 30 and mes == 2:
        return True
    else:
        return False
    
    

dias = tuple(range(1, 32))
meses = tuple(range(1, 13))
anios = tuple(range(1, 2200))
anios_bisiestos = tuple(range(1584, 2100, 4))


print(verificar_fecha_valida(12, 12, 2004))