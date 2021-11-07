# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1- O nome com todas as letras maiúsculas
# 2- O nome com todas minúsculas
# 3- Quantas letras no total (sem considerar espaços).
# 4- Quantas letras tem o primeiro nome

nomecompleto = input('Digite o seu nome completo: ').strip()

print(nomecompleto.upper())
print(nomecompleto.lower())

nomes = nomecompleto.split()
# nomecompletosemespaco = ''.join(nomes)
# print('Tem {} letras sem contar espaço'.format(len(nomecompletosemespaco)))

print('Seu nome tem {} letras'.format(len(nomecompleto) - nomecompleto.count(' ')))

print('Tem {} letras no primeiro nome'.format(len(nomes[0])))
print('Seu primeiro nome tem {} letras'.format(nomecompleto.find(' ')))

