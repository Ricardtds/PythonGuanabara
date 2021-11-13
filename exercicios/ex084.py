# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.

# B) Uma listagem com as pessoas mais pesadas.

# C) Uma listagem com as pessoas mais leves.

pessoas = []
pessoa = []
pessoamaiorpeso = []
pessoamenorpeso = []
while True:
    pessoa.append(str(input('Digite seu nome: ')))
    pessoa.append(float(input('Digite o seu peso: ')))
    pessoas.append(pessoa[:])
    if len(pessoas) == 1:
        menorpeso = maiorpeso = pessoa[1]
    else:
        if menorpeso > pessoa[1]:
            menorpeso = pessoa[1]
        if maiorpeso < pessoa[1]:
            maiorpeso = pessoa[1]
    pessoa.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
        if opcao in 'sn':
            break
    if opcao in 'n':
        break

for pessoa in pessoas:
    if menorpeso == pessoa[1]:
        pessoamenorpeso.append(pessoa[0])
    if maiorpeso == pessoa[1]:
        pessoamaiorpeso.append(pessoa[0])

print(f'Tivemos um total de {len(pessoas)} pessoas cadastradas.')
print(f'O maior peso foi de {maiorpeso:.2f}Kg. Peso de {pessoamaiorpeso}')
print(f'O menor peso foi de {menorpeso:.2f}Kg. Peso de {pessoamenorpeso}')
