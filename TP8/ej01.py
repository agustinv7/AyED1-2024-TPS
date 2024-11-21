meses = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

hora_valida = tuple(i for i in range(0, 24))
minutos_validos = tuple(i for i in range(0, 60))


def verificacion_input(mensaje: str) -> int:
    while True:
        try:
            dato = int(input(mensaje))
            return dato
        except Exception("Error") as e:
            print(f"Error:{e}")


def verificar_n(n: int) -> bool:
    """
    Args:
        n (int): recibe como parametro un número entero

    Returns:
        bool: retorna true si se cumple la condicion si es natural, caso contrario, false
    """
    while True:
        try:
            if n > 0:
                return bool
        except ValueError:
            print("Error")


# A


def anio_bisiesto(anio: int) -> bool:
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def verificar_fecha_valida(anio: int, mes: int, dia: int) -> tuple:
    fecha = (
        1,
        1,
        1,
    )
    if anio_bisiesto(anio):
        if meses.get(mes) and 1 <= dia <= meses[mes]:
            fecha = (
                anio,
                mes,
                dia,
            )
            return fecha


# B
def sumar_dias(dias: int, anio: int, mes: int, dia: int) -> tuple:
    fecha = list(verificar_fecha_valida(anio, mes, dia))
    fecha[-1] += dias
    while fecha[-1] > meses[mes]:
        fecha[-1] -= meses[mes]
        fecha[-2] += 1
        if fecha[-2] > 12:
            fecha[-2] = 1
            fecha[0] += 1
    return tuple(fecha)


# C
def verificar_horario(hora: int, minutos: int) -> bool:
    horario = False
    if hora in hora_valida and minutos in minutos_validos:
        horario = True
    return horario


# D
def sumar_horarios(hora_1: int, minuto_1: int, hora_2: int, minuto_2: int) -> None:
    horario_1 = verificar_horario(hora_1, minuto_1)
    horario_2 = verificar_horario(hora_2, minuto_2)
    diferencia_horas = 0
    diferencia_minutos = 0
    if horario_1 and horario_2:
        if hora_1 >= hora_2:
            diferencia_horas = hora_1 - hora_2
        elif hora_2 >= hora_1:
            diferencia_horas = hora_2 - hora_1
        if minuto_1 >= minuto_2:
            diferencia_minutos = minuto_1 - minuto_2
        elif minuto_2 >= minuto_1:
            diferencia_minutos = minuto_2 - minuto_1
        if diferencia_horas < 24:
            print()
            print(
                f"La diferencia entre {hora_1}:{minuto_1} y {hora_2}:{minuto_2} es de {diferencia_horas}h y {diferencia_minutos}m"
            )
        else:
            print("La diferencia de horas es mayor a 24")
    return None


def menu() -> None:
    opciones = [
        "Fecha valida",
        "Sumar N dias",
        "Ingresar un horario",
        "Calcular 2 horarios",
        "Salir",
    ]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                anio = verificacion_input("Ingrese el anio: ")
                mes = verificacion_input("Ingrese el mes: ")
                dia = verificacion_input("Ingrese el dia: ")
                print(verificar_fecha_valida(anio, mes, dia))
            case 2:
                anio = verificacion_input("Ingrese el anio: ")
                mes = verificacion_input("Ingrese el mes: ")
                dia = verificacion_input("Ingrese el dia: ")
                dias = verificacion_input("Ingrese los dias a sumar: ")
                print(sumar_dias(dias, anio, mes, dia))
            case 3:
                hora = verificacion_input("Ingrese la hora: ")
                minutos = verificacion_input("Ingrese los minutos: ")
                print(verificar_horario(hora, minutos))
            case 4:
                hora_1 = verificacion_input("Ingrese la primer hora: ")
                minuto_1 = verificacion_input("Ingrese los primeros minutos: ")
                hora_2 = verificacion_input("Ingrese la segunda hora")
                minuto_2 = verificacion_input("Ingrese las segundas horas: ")
                sumar_horarios(hora_1, minuto_1, hora_2, minuto_2)
            case _:
                print("Opcion no valida. \n")
        return None


if __name__ == "__main__":
    menu()
