# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

lista = []
listainterna = []
totpares = totterceiracoluna = 0
for x in range(3):
    for i in range(3):
        listainterna.append(int(input(f'Digite o número na posição [{x}][{i}]: ')))
    lista.append(listainterna[:])
    listainterna.clear()

maiorvalor = lista[1][0]

for posx, x in enumerate(lista):
    for posy, i in enumerate(x):
        print(f'[{i}]', end=' ')
        if i % 2 == 0:
            totpares += i
        if posy == 2:
            totterceiracoluna += i
        if posx == 1 and maiorvalor < i:
            maiorvalor = i

    print()

print(f'A soma de todos os pares dá: {totpares}')
print(f'A soma da terceira coluna dá: {totterceiracoluna}')
print(f'O maior valor da segunda linha {maiorvalor}')