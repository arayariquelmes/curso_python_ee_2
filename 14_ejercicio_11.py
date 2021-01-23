#Escribir un programa que pida al usuario un número entero positivo
#y muestre por pantalla la cuenta atrás desde ese 
#número hasta cero separados por comas.

n = -1
while n <=0:
    print("Ingrese un número positivo:")
    n = int(input())

i = n

while i>=0:
    final = ','
    if i ==0:
        final ='\n'
    print(i, end=final)
    i-=1