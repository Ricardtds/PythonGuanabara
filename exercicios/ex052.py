# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número inteiro: '))
qtd_divisores = 0

for x in range(1, numero):
    if numero % x == 0:
        qtd_divisores += 1

if qtd_divisores == 1:
    print('O número {} é primo!'.format(numero))
else:
    print('O número {} não é primo'.format(numero))
