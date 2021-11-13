# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

# No final, mostre a matriz na tela com a formatação correta
lista = []
listainterna = []
for x in range(3):
    for i in range(3):
        listainterna.append(int(input(f'Digite o número na posição [{x}][{i}]: ')))
    lista.append(listainterna[:])
    listainterna.clear()

for x in lista:
    for i in x:
        print(f'[{i}]', end=' ')
    print()


