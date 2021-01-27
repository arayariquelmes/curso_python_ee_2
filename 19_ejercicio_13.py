#Generar una lista con las letras del
#abecedario, posteriormente generar otra
#lista con solo las letras  que se encuentran en
#posiciones pares de la lista original.

#abecedario = []
#for i in range(ord('a'), ord('z') + 1):
#    abecedario.append(chr(i))
abecedario = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(abecedario)

#abcPar = []
#for i in range(len(abecedario)):
#    if i % 2 == 0:
#        abcPar.append(abecedario[i])

abcPar = [abecedario[i] for i in range(len(abecedario)) if i % 2 == 0]
print(abcPar)