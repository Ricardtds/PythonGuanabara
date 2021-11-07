# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# EX: Ana Maria de Souza
# Primeiro: ANA
# ÚLTIMO: Souza

nome = str(input('Digita o seu nome: '))
nome = nome.split()
print('O primeiro nome é: {}'.format(nome[0]))
print('O ultimo nome é: {}'.format(nome[len(nome)-1]))
