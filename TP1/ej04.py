"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos  números  enteros,  correspondientes  al total  de  la compra  y  al  dinero  recibido. 
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
de $5000, $1000, $500, $200, $100, $50 y  $10. Emitir un mensaje de  error  si el 
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
billete de $200, 1 billete de $100 y 3 billetes de $10
"""


def transaccion(total_compra: int, dinero_recibido: int) -> int:
    """
    total_compra: este dato debe ser un numero positivo de tipo int y refleja el monto
                que el cliente tiene que pagar por la compra de los electrodomesticos

    dinero_recibido: este dato debe ser un numero positivo de tipo int y recibe el monto
                    que el cliente dio a cambio del total de la compra.

    Para que la funcion se pueda ejecutar, el dinero recibido debe ser mayor al total de la compra
    y para que se pueda emitir el cambio correctamente, el total de la compra debe ser
    multiplo de 10
    """
    vuelto = []
    billetes = []
    tupla_billetes = (5000, 1000, 500, 200, 100, 50, 10)
    resto = (
        dinero_recibido - total_compra
    )  # en esta variable guardo resto el dinero recibido con el total de la compra
    if dinero_recibido > total_compra and total_compra % 10 == 0:
        # en esta linea verifico si el dinero con el que se paga es mayor al total de la compra
        # también verifico si el total de la compra es múltiplo de 10, en el caso de no ser así,
        # no se podrá emitir el cambio
        for i in tupla_billetes:
            # recorro cada índice de la tupla
            if resto >= i:
                # verifico si el resto es mayor o igual al [i] en cada iteracion
                vuelto.append(resto // i)
                # appendeo las veces que el valor que está en el resto entre en el [i]
                billetes.append(i)
                # appendeo el valor del billete
                resto = resto % i
                # el nuevo resto se calcula con el módulo de [i]
        print(
            vuelto, billetes
        )  # aca printeo para ver las listas finales, no se como podría mostrar el msj final
    else:
        print("Error")
    return None


def verificacion_valores(total_compra: int, dinero_recibido: int) -> bool:
    """
    Esta funcion verifica si los parámetros son válidos
    """
    if (total_compra and dinero_recibido) > 0:
        return True
    else:
        return False


def menu():
    while True:
        total_compra = int(input("Ingrese el total de la compra: "))
        dinero_recibido = int(input("Ingrese el monto con el que pagará: "))
        if verificacion_valores(total_compra, dinero_recibido):
            transaccion(total_compra, dinero_recibido)
            break
        else:
            print("Los datos son erroneos")


menu()
