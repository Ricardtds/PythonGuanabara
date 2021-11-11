# Faça um programa que jogue par ou ímpar com o computador. O jogo só será inteerrompido quando o jogador Perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0
while True:
    numero_pc = randint(0, 10)
    while True:
        opcao_jogador = str(input('Digite par ou impar: ')).strip().lower()
        if opcao_jogador == 'par' or opcao_jogador == 'impar':
            break
    numero_jogador = int(input('Digite um número inteiro: '))
    if (numero_pc + numero_jogador) % 2 == 0:
        if opcao_jogador == 'par':
            print(f'Você jogou {numero_jogador} e o computador jogou {numero_pc} então você venceu pois deu par!')
            vitorias += 1
        elif opcao_jogador == 'impar':
            print(f'Você jogou {numero_jogador} e o computador jogou {numero_pc} então você perdeu pois deu par!')
            break
    else:
        if opcao_jogador == 'impar':
            print(f'Você jogou {numero_jogador} e o computador jogou {numero_pc} então você venceu pois deu ímpar!')
            vitorias += 1
        elif opcao_jogador == 'par':
            print(f'Você jogou {numero_jogador} e o computador jogou {numero_pc} então você perdeu pois deu ímpar!')
            break

print(f'Voce obteve um total de {vitorias} vitórias no jogo!')
