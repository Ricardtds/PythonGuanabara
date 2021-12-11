# Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um istema de visualização de detalhes do
# aproveitamento de cada jogador.

elenco = list()

while True:
    jogador = {
        'nome': str(input('Digite o nome: ')),
        'partidas': int(input('Digite quantas partidas: '))
    }
    qtd_gols = []
    tot_gols = 0
    for i in range(jogador['partidas']):
        gols = int(input(f'Quantos gols fez na partida {i+1}? '))
        qtd_gols.append(gols)
        tot_gols += gols
    jogador['gols por partida'] = qtd_gols
    jogador['total de gols'] = tot_gols
    elenco.append(jogador)
    vaicontinuar = str(input('Quer continuar[S/N]? ')).upper()[0]
    while vaicontinuar[0] not in 'SN':
        vaicontinuar = str(input('Digite S ou N: '))
    if vaicontinuar[0] in 'Nn':
        break

print('-=' * 40)
print(f'{"Cod":<4} {"Nome":<13} {"Gols":<20} {"Total":}')
for i, v in enumerate(elenco):
    print(
        f'{str(i):<4} {v["nome"]:<13} {str(v["gols por partida"]):<20} {v["total de gols"]}')
