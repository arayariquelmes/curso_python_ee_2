#Escribir un programa que reciba 2 valores enteros  y
#una operación string, dependiendo de la operación ejecutar
#la suma, resta,
#multiplicación o división entre los valores

print("Ingrese numero 1:")
n1 = int(input())
print("Ingrese numero 2:")
n2 = int(input())
print("Ingrese operacion:")
op = input().lower() #SuMa
if op == "suma":
    print(n1 + n2)
elif op == "resta":
    print(n1 - n2)
elif op == "multiplicacion":
    print(n1 * n2)
elif op == "division":
    if n2 == 0:
        print("No puede dividir por 0")
    else:
        print(n1 / n2)
else:
    print("Operador incorrecto")
