#Crear un archivo conversor.py que contenga un programa
#que convierta de centímetros a pulgadas. Una pulgada es 
# igual a 2.54 centímetros.

print("Ingrese valor en centimetros:")
cm = float(input())
pulgadas = cm/2.54
print(f"El valor {cm} centimetros equivale a {round(pulgadas,2)} pulgadas")
