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


nombres_meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}


def verificacion_input(mensaje: str) -> int:
    while True:
        try:
            dato = int(input(mensaje))
            return dato
        except Exception("Error") as e:
            print(f"Error:{e}")
            return verificacion_input(mensaje)


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


def crear_fecha(fecha: tuple) -> str:
    dia, mes, anio = fecha
    mes_electo = 0
    terminacion_anio_1900 = "19" + (str(anio))
    terminacion_anio_2000 = "20" + (str(anio))
    mes_electo = nombres_meses.get(mes)
    if anio > 30:
        return f"{dia} de {mes_electo} de {terminacion_anio_1900}"
    return f"{dia} de {mes_electo} de {terminacion_anio_2000}"


def menu() -> None:
    opciones = ["Fecha válida", "Salir"]
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i+1} - {opcion}")
        ingresar_opcion = int(input("Ingrese su opcion: "))
        match ingresar_opcion:
            case 1:
                dia = verificacion_input("Ingrese el dia: ")
                mes = verificacion_input("Ingrese el mes: ")
                anio = verificacion_input("Ingrese el anio: ")
                fecha = dia, mes, anio
                print(crear_fecha(fecha))
            case 2:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida. \n")
        return None


if __name__ == "__main__":
    menu()
