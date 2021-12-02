# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
lista = list()
jogador = dict()
ranking = list()
for x in range(4):
    jogador['Nome'] = 'jogador'+str(x+1)
    jogador['Dado'] = randint(1, 6)
    lista.append(jogador.copy())
del jogador

print("Valores sorteados: ")
for x in lista:
    print(f'    O {x["Nome"]} tirou {x["Dado"]}')
    sleep(1)

k = 1
for t in range(len(lista)):
    for x in range(len(lista)-k):
        while lista[x]['Dado'] < lista[x+1]['Dado']:
            auxiliar = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = auxiliar
    k += 1

print("Ranking dos jogadores: ")
for pos, item in enumerate(lista):
    print(f'    {pos+1}o lugar: O {item["Nome"]} com {item["Dado"]}')
    sleep(1)


jogo = {
    'jogador0': randint(1, 6),
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6)
}
print(jogo)
for c in range(len(jogo)-1):
    for k in range(len(jogo)-1-c):
        if jogo[f'jogador{k}'] > jogo[f'jogador{k+1}']:
            aux = jogo[f'jogador{k}']
            jogo[f'jogador{k}'] = jogo[f'jogador{k+1}']
            jogo[f'jogador{k+1}'] = aux


print(jogo)
