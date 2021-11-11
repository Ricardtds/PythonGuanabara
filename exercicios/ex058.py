# Escreva um programa que faça o computador "pensar" em um número inteiro entre
# 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número
# entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar
# mostrando no final quantos palpites foram necessário para vencer.

from random import randint
numeropc = randint(0, 10)

# print(numeropc)
acertou = -1
count = 0

while acertou != numeropc:
    acertou = int(input('Digite um número entre 0 e 10: '))
    count += 1

print('Parabéns, você levou {} tentativas'.format(count))
