# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o
# vencedor tirou o maior número no dado.
from time import sleep
from random import randint

lista = list()
jogador = dict()


for x in range(4):
    jogador['Nome'] = 'jogador'+str(x+1)
    jogador['Dado'] = str(randint(1, 6))
    lista.append(jogador.copy())
del jogador

print("Valores sorteados: ")
for i, v in enumerate(lista):
    print(f'O {v["Nome"]} tirou {v["Dado"]}')
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
