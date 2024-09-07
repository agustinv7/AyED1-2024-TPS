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

def transaccion(total_compra: int, dinero_recibido:int) -> int:
    """
    total_compra: este dato debe ser un numero positivo de tipo int y refleja el monto
                que el cliente tiene que pagar por la compra de los electrodomesticos
                
    dinero_recibido: este dato debe ser un numero positivo de tipo int y recibe el monto
                    que el cliente dio a cambio del total de la compra.
                    
    retorna dato de tipo int
    
    Para que la funcion se pueda ejecutar, el dinero recibido debe ser mayor al total de la compra 
    y para que se pueda emitir el cambio correctamente, el total de la compra debe ser 
    multiplo de 10
    """
    vuelto = []
    billeteee = []
    billetes = (5000, 1000, 500, 200, 100, 50, 10)
    resto = dinero_recibido - total_compra
    
    
    if total_compra > dinero_recibido:
        pass
    elif total_compra % 10 != 0:
        pass
    else:
        for billete in billetes:
            if resto >= billete:
                vuelto.append(resto//billete)
                billeteee.append(billete)
                resto = resto % billete
    return vuelto, billeteee

               
print(transaccion(12500, 20000))            