# Faça um programa que ajude um jogador da MEGA Sena a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrandoo tudo em uma lista composta.

from random import randint as sorteio
from time import sleep
qtdjogos = int(input('Quantos jogos serão gerados? '))
qtdpalpites = int(input('Quantos palpites por jogo? '))
lista = []
numerossorteados = []
for x in range(qtdjogos):
    for i in range(qtdpalpites):
        while True:
            numerosorteado = sorteio(1, 60)
            if numerosorteado not in numerossorteados:
                break
        numerossorteados.append(numerosorteado)

    numerossorteados.sort()
    lista.append(numerossorteados[:])
    numerossorteados.clear()

for pos, x in enumerate(lista):
    print(f'O jogo {pos+1} teve os números: {x} sorteados!')
    sleep(1)
