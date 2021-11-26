# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint

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
