#Ejemplo de definición de funciones

def saludar(nombre="Seba", edad=32):
    print("Tu nombre es",nombre,"y tu edad es", edad)

saludar()
saludar("Pablo",17)
saludar("Cesar")
saludar()
saludar(edad=10)

def calcularArea():
    base = int(input("Ingrese base:"))
    altura = int(input("Ingrese estatura:"))
    print(base*altura)
calcular