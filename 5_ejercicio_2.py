# 2. Escribir un programa que pregunte 
# el nombre del usuario en la consola y 
# después de que el usuario lo introduzca 
# muestre por pantalla la cadena 
# ¡Hola <nombre>!, donde <nombre> es el 
# nombre que el usuario haya introducido.

print("Ingrese nombre de usuario:")
nombre = input()
nombre = nombre.strip()
print(f"Hola {nombre}!")