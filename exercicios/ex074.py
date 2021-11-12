# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

# Depois disso mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla.

from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = numeros[0]
print('Os valore sorteados foram: ', end='')

for x in numeros:
    print(x, end=' ')
    if maior < x:
        maior = x
    if menor > x:
        menor = x
print()
print(f'O maior número da função max foi: {max(numeros)}')
print(f'O menor número da função min foi: {min(numeros)}')
print(f'O maior número do loop foi: {maior}')
print(f'O menor número do loop foi: {menor}')
