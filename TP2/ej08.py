"""
Utilizar  la  técnica  de  listas  por  comprensión  para  construir  una  lista  con  todos  los 
números impares comprendidos entre 100 y 200
"""
numeros_impares = [i for i in range(100, 200) if i % 2 != 0]
#en esta linea itero cada elemento entre 100 y 200. Si cumple con la condicion, se queda en la lista
print(numeros_impares)