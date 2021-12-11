# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas

# B) A média de idade do grupo.

# C) Uma lista com todas as mulheres.

# D) Uma lista com todas as pessoas com idade acima da média.

comunidade = list()
pessoa = dict()
tot_idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite teu nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite seu sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Responda apenas M ou F')
    pessoa['idade'] = int(input('Digite sua idade: '))

    tot_idade += int(pessoa['idade'])

    comunidade.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if continuar in 'N':
        break
del pessoa
print()
print(f'Foram cadastradas {len(comunidade)} pessoas')
media = tot_idade/len(comunidade)
print(f'A média de idade do grupo foi: {media}')

print('A lista de mulheres: ')
for i in comunidade:
    if i['sexo'] in 'Ff':
        print(i)
print('Pessoas acima da media: ')
for i in comunidade:
    if float(i['idade']) > media:
        print(i)
