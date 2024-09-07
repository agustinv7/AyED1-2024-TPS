"""
Una persona  desea  llevar  el control de  los gastos  realizados  al  viajar  en  el  subte-
rráneo  dentro  de  un  mes.  Sabiendo  que  dicho  medio  de  transporte  utiliza  un  es-
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro-
llar una función que reciba como parámetro la cantidad de viajes realizados en un 
determinado  mes  y  devuelva  el  total  gastado  en  viajes.  Realizar  también  un  pro-
grama para verificar el comportamiento de la función    
"""


def control_de_gastos_viajes(viajes: int, tarifa: int) -> float:
    #la funcion ingresa 2 parametros de tipo entero y devuelve un resultado de tipo flotante
    while True:
        #utilizo un while true para ingresar al bucle
        if viajes > 0:
        #si viajes es mayor a 0 ingresa a verificar que cantidad de viajes se hicieron
            if viajes > 40:
                return viajes * (0.60 * tarifa)
            elif viajes > 30 and viajes < 41:
                return viajes * (0.70 * tarifa)
            elif viajes > 20 and viajes < 31:
                return viajes * (0.80 * tarifa)
            elif viajes > 0 and viajes < 21:
                return viajes * (1.0 * tarifa)
        else:
            return "Error"    


def comprobacion(viajes: int, tarifa: int) -> None:
    assert(type(viajes) == int)
    assert(type(tarifa) == int)
    return None


print(control_de_gastos_viajes(2, 400))

comprobacion(2, 400)