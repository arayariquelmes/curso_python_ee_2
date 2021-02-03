#Escriba una función que reciba un
#valor analógico entre 0 y 1023 y
#retorne el calculo de temperatura equivalente para un
#sensor tm36: TEMP = ((VA*5,0)/1024 – 0,5) * 100
from funciones import calcularTemp
n = -1
while n <0 or n > 1023:
    try:
        print("Ingrese valor analogico:")
        n = int(input())
    except:
        n = -1
        print("El valor debe ser numerico")

print("La temperatura es", calcularTemp(n))
