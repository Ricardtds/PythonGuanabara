# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação. Depois mostre:

# Apenas os 5 primeiros colocados.

# Os últimos 4 colocados tabela.

# Uma lista com os times em ordem alfabética.

# Em que posição na tabela está o time da chapecoense.

tabelabrasileirao = ('Atlético Mineiro', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Internacional',
          'Fluminense', 'Athletico-PR', 'América-MG', 'Cuiabá', 'Ceará', 'Santos', 'São Paulo', 'Atlético Goiano',
          'Bahia', 'Juventude', 'Sport Recife', 'Grêmio', 'Chapecoense')

print(f'Os 5 primeiros {tabelabrasileirao[:5]}')
print(f'Os 4 últimos {tabelabrasileirao[-4::1]}')
print(f'Tabela Organizda: {sorted(tabelabrasileirao)}')
print(f'O chapecoense está na posição {tabelabrasileirao.index("Chapecoense") + 1}')
