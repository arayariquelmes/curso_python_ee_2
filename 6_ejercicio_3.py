
#3. Escribir un programa que solicite base y 
#estatura de un triangulo y muestre por pantalla su área, 
#formula: base*altura/2

print("Ingrese base:")
base = int(input())
print("Ingrese altura:")
altura = int(input())

area = base*altura/2
print("El area del triangulo es {0}".format(round(area,2)))