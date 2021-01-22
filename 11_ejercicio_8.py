#Genere un archivo llamado repetir.py que solicite al usuario
#una palabra y una cantidad. Posteriormente debe mostrar por
#pantalla la palabra
#repetida la cantidad de veces escrita.

print("Digame una palabra:")
palabra = input()
print("Ingrese cantidad de repeticiones:")
cantidad = int(input())

i = 0

while i < cantidad:
    print(palabra)
    i+=1 #i=i+1

#Forma Python
print("Forma python")
print((palabra+"\n")*cantidad)