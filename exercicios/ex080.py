# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

numeros = list()
for x in range(5):
    numero = int(input('Digite um número: '))
    index = len(numeros)
    if x == 0:
        numeros.append(numero)
    else:
        for pos, item in enumerate(numeros):
            if numero < item:
                index = pos
                break
        numeros.insert(index, numero)
print(numeros)
