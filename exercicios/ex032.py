# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
ano = int(input('Digite um ano qualquer: '))

if ano == 0:
    ano = date.today().year
print('Ano escolhido: {}'.format(ano))

if ano % 4 == 0 and ano % 100 != 0:
    print('É um ano bissexto')
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')

