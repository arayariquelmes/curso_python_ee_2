#Generar un programa en python que genere una lista de 10 números al azar entre 1 y 20.


from random import randint

#Esto es lo mismo que la compresión
#lista = []
#for i in range(10): 
#    lista.append(randint(1,20))

lista = [randint(1,20) for i in range(10)]
print(lista)
#[1,6,10,80,2,5,5]
#En base al ejercicio anterior, solicitar al usuario 10 números y mostrar cuantos aciertos tuvo
#al adivinar los números de la lista original.
aciertos = 0
for i in range(10):
    print("Ingrese número a adivinar:")
    n = int(input())
    if n in lista:
        aciertos+=1

print("La cantidad de aciertos fue",aciertos)