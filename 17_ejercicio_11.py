#Escribir un programa que almacene 
#en una lista los números del 1 al 10 y los
#muestre por pantalla en orden inverso separados
#por comas.

lista = []
for i in range(10):
    n = int(input("Ingrese número " + str(i + 1) + ":"))
    lista.append(n)
print(lista)
lista.reverse()
print(lista)
#for n in reversed(lista):
#    print(n, end=",")
