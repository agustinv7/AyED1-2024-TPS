"""
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
cada  uno  puede  transportar  hasta  media  tonelada  (500  kilogramos).  En  un  cajón 
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
de  alguna  naranja  se  encuentra  fuera  del  rango  indicado  se  la  clasifica  para 
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
jugo y  si hay  algún sobrante  de naranjas que  deba  considerarse para  el siguiente 
reparto. Simular el peso de cada unidad generando un número entero al azar entre 
150 y 350.
Además,  se  desea  saber  cuántos  camiones  se  necesitan  para  transportar  la  cose-
cha,  considerando  que  la  ocupación  del  camión  no  debe  ser  inferior  al  80%;  en 
caso contrario el camión no serán despachado por su alto costo. 

"""

import random as rn


def calcular_cajones_naranjas(
    cosecha_a_procesar: int, peso_min: int, peso_max: int
) -> tuple:
    """
    Esta funcion recibe como parámetros un numero entero indicando de las naranjas a procesar,
    peso mínimo y máximo que son los gramos que tiene que pesar cada naranja para seleciconarla
    Lo que hace esta función es iterar por el parámetro que le pasemos
    Dentro de la iteración, se dictará de manera aleatoria el peso de las naranjas
    Si el peso es entre 200 y 300 gramos, son naranjas de cosecha, caso contrario, de jugo
    Retorna una tupla con las naranjas de jugo y de cosecha
    """
    for _ in range(cosecha_a_procesar):
        # ingreso en el for para calificar cada naranja
        global naranjas_cosecha, naranjas_jugo
        # invoco a global porque no se por que motivo no me toma bien la variable naranjas?cosecha
        naranjas = rn.randint(150, 350)
        # genero el peso aleatorio de la naranja
        if naranjas < peso_min or naranjas > peso_max:

            naranjas_jugo += 1
        else:
            naranjas_cosecha += 1
    return naranjas_jugo, naranjas_cosecha


def calcular_camiones(naranjas_cosecha: int) -> tuple:
    """
    En esta funcion se recibe el numero de las naranjas para cosecha, dato tipo entero
    Dentro de esta funcion, se calculan los cajones, resto de naranjas, cajones por camion
    camiones necesarios y cajones restantes.
    Se retorna una tupla
    """
    # global naranjas_por_cajon, peso_max, peso_min, cajones_llenos, cajones_restantes
    cajones_llenos = naranjas_cosecha // naranjas_por_cajon
    resto_naranjas = naranjas_cosecha % naranjas_por_cajon
    cajones_por_camion = 5
    camiones_necesarios = cajones_llenos // cajones_por_camion
    cajones_restantes = cajones_llenos % cajones_por_camion

    if cajones_restantes / cajones_por_camion >= 0.8:
        # si la division entre los cajones restantes y cajones por camion es mayor al 80%
        # se necesita un camion
        camiones_necesarios += 1

    print(f"Se llenaron {cajones_llenos} cajones con naranjas de cosecha")
    print(f"{cajones_restantes} cajones quedaron sin cargar")
    print(f"{resto_naranjas} son las naranjas sobrantes\n")

    if camiones_necesarios == 1:
        print(f"Se necesita 1 camion")
    else:
        print(f"Se necesitan {camiones_necesarios} camiones ")

    datos_finales = (cajones_restantes, resto_naranjas, camiones_necesarios)
    # guardo estos datos en una tupla y los retorno
    return datos_finales


peso_min = 200
peso_max = 300
naranjas_por_cajon = 100
camiones_necesarios = 0
naranjas_cosecha = 0
naranjas_jugo = 0
cajones_llenos = 0
resto_naranjas = 0
cajones_restantes = 0

cosecha_a_procesar = int(input("Ingrese el numero de naranjas a cosechar: "))
# se ingresa a mano el dato de cosechas de naranjas a procesar
calcular_cajones_naranjas(cosecha_a_procesar, peso_min, peso_max)
print(f"Son {naranjas_jugo} naranjas para jugo\n")
calcular_camiones(naranjas_cosecha)
