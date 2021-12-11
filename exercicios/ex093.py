# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e
# Quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em
# cada partida. No final, tudo isso será
# Guardado em um dicionã́rio, incluindo o total de gols feitos
# durante o campeonato.

jogador = {
    'nome': str(input('Nome: ')),
    'partidas': int(input('Quantas partidas: '))
}
partidas = []
for i in range(jogador['partidas']):
    gols = int(input(f'Quantos gols fez na partida {i+1}? '))
    partidas.append(gols)
jogador['gols por partida'] = partidas
jogador['total de gols'] = sum(partidas)

print(jogador)
