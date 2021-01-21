# 1. Escriba un programa en Python que calcule
# el promedio de tres notas
# El programa debe solicitar cada nota y
# entregar el resultado.

print("Ingrese nota 1:")
n1 = float(input())
print("Ingrese nota 2:")
n2 = float(input())
print("Ingrese nota 3:")
n3 = float(input())

prom = (n1 + n2 + n3)/3
print("El promedio es:",round(prom,2))