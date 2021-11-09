# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com uma pausa de 1segundo entre eles.

from time import sleep

print('{:-^50}'.format(''))
for x in range(10, -1, -1):
    print('{}...'.format(x))
    sleep(1)

print('Fogos Fogos Fogos')
