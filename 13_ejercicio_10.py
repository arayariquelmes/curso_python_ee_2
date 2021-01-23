#Escribir un programa que pida al
#usuario un número entero positivo y muestre por pantalla
#todos los números impares desde 1 hasta ese número separados por comas.

n = -1
while n <=0:
    print("Ingrese número positivo:")
    n = int(input())

i =1 # 1 2 3 4 ...N
if n % 2==0:
    n-=1 #n = n -1
while i <=n:
    final = ','
    if i == n:
        final = '\n'
    if i % 2 != 0:
        print(i, end=final)
    i+=1
