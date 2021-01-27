#Escribir un programa en Python que reciba una lista
#de 5 medidas de temperatura (entre -20 y 80).
#Posteriormente mostrar las siguientes opciones:
#Mostrar la mayor temperatura registrada
#Mostrar la menor temperatura registrada
#Mostrar el promedio de temperaturas
#Mostrar las temperaturas en orden descendente

temps = []
for i in range(5):
    t = -900
    while t < -20 or t >80:
        try:
            print("Ingrese medida de temperatura", i + 1)
            t = float(input())
        except:
            t= -900
            print("La temperatura debe ser un número")
    temps.append(t)
print(temps)
print("La mayor temperatura registrada es", max(temps))
print("La menor temperatura registrada es", min(temps))
print("El promedio de las temperaturas es", round(sum(temps)/len(temps),2))
temps.sort()
temps.reverse()
print("En orden descendente",temps)


