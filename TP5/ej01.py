"""
Desarrollar  una  función  para  ingresar  a  través  del  teclado  un  número  natural.  La 
función  rechazará  cualquier  ingreso  inválido  de  datos  utilizando  excepciones  y 
mostrará  la  razón  exacta  del  error.  Controlar  que  se  ingrese  un  número,  que  ese 
número  sea  entero  y  que  sea  mayor  que  0,  mostrando  un  mensaje  con  la  razón 
exacta  del  error  en  caso  necesario.  Devolver  el  valor  ingresado  cuando  éste  sea 
correcto.  Escribir  también  un  programa  que  permita  probar  el  correcto  funciona-
miento de la misma
"""


def ingresar_numero_natural() -> int:
    """
    En esta funcion se pide un numero natural mayor a 0
    Se verifica si no hay errores como ingreso de caracteres
    alfabeticos, caracteres especiales y numeros racionales
    """
    while True:
        numero = input("Ingrese un numero: ")
        try:
            valor = int(numero)
        except ValueError:
            print(f"ValueError, '{numero}' no es un numero entero")
        else:
            return valor


print(ingresar_numero_natural())
