# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if maior < n3:
    maior = n3

if menor > n3:
    menor = n3

print('O menor valor foi: {}'.format(menor))
print('O maior valor foi: {}'.format(maior))
