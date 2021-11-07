# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo

n1 = float(input('Digite o lado 1: '))
n2 = float(input('Digite o lado 2: '))
n3 = float(input('Digite o lado 3: '))

if n1 > n2:
    maior = n1
    lado1 = n2
    lado2 = n3
else:
    maior = n2
    lado1 = n1
    lado2 = n3

if maior < n3:
    maior = n3
    lado1 = n1
    lado2 = n2

if maior >= (lado1 + lado2):
    print('Não é possível fazer um triangulo')
else:
    print('É possível fazer o triangulo')

