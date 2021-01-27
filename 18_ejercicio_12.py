#Generar un programa que reciba los nombres de 10 personas.
#Posteriormente solicitar el nombre de una persona e indicar
#si se encuentra en la lista o no.

nombres = []
for i in range(1,5):
    print("Ingrese persona nro",i)
    nombre = input()
    nombres.append(nombre)

print(nombres)
buscado = "a"
while buscado != "":
    print("Ingrese nombre que busca:")
    buscado = input()
    if buscado != "":
        if buscado in nombres:
            print("Si se encuentra en la lista")
        else:
            print("No se encuentra en la lista")