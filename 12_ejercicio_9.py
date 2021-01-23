#Escriba un programa que pida al
#usuario ingresar la altura y el ancho de un rectángulo
#y lo dibuje utilizando asteriscos

print("Ingrese altura:")
altura = int(input())
print("Ingrese ancho:")
ancho = int(input())

i = 0
while i < altura:
    j=0
    while j < ancho:
        print('*', end='')
        j+=1
    i+=1
    print()

print("Forma Python:")
#Forma Python:
print((('*'*ancho) + '\n') * altura)