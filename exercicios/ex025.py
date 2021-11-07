# Crie um programa que leia o nome de uma pessoa e diga sela tem "Silva" no nome

nome = input('Digite o seu nome: ').strip().title()
print(nome)
print('{} para SILVA no nome'.format('Silva' in nome))
