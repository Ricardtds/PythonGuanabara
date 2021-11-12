# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação. Depois mostre:

# Apenas os 5 primeiros colocados.

# Os últimos 4 colocados tabela.

# Uma lista com os times em ordem alfabética.

# Em que posição na tabela está o time da chapecoense.

tabela = ('Atlético Mineiro', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Internacional',
          'Fluminense', 'Athletico-PR', 'América-MG', 'Cuiabá', 'Ceará', 'Santos', 'São Paulo', 'Atlético Goiano',
          'Bahia', 'Juventude', 'Sport Recife', 'Grêmio', 'Chapecoense')

print(tabela[:5])
print(tabela[-4::1])
print(sorted(tabela))
print(tabela.index("Chapecoense"))
