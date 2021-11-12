# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.

palavras = ('Planta', 'Detetive', 'Tesouro', 'Prisma', 'Enterrar', 'Local')

for pos, item in enumerate(palavras):
    print(f'A palavra {item} tem as vogais: ', end='')
    for x in range(len(item)):
        if item[x] in 'AaEeIiOoUu':
            print(item[x], end=' ')
    print()