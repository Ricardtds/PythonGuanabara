# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar

numero = int(input('Digite um número inteiro: '))

print('Você digitou o número {}'.format(numero))
if numero % 2 == 0:
    print('Ele é par')
else:
    print('Ele é impar')
