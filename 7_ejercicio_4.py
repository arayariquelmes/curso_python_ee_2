# 4. Genere un script en python que
# solicite al usuario un valor entre 0 y 1023
# (correspondiente a la lectura analoga de un sensor tm36)
# y muestre por pantalla el valor de temperatura
# en grados Celsius equivalente.
# Considerando que el valor entregado esta en
# la variable VA, el valor de temperatura es
# equivalente al resultado de la siguiente formula:
# TEMP = ((VA*5,0)/1024 – 0,5) * 100
print("Ingrese valor analogico:")
va = int(input())
temp = ((va*5.)/1024 - .5) * 100
print("El valor de temp es:",round(temp,2)," Celsius")