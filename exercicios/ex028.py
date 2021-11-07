# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numero_sorteado = randint(0, 5)
tentativa = int(input('Adivinhe o número entre 0 e 5: '))

print('Deixa eu conferir...')
sleep(2)

if tentativa == numero_sorteado:
    print('Parabéns você acertou!')
else:
    print('Não foi dessa vez.')
