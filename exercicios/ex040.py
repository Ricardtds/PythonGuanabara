# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:

# - Média abaixo de 5.0 : Reprovado
# - Média entre 5.0 e 6.9 : Recuperação
# - Média entre 7.0 ou superior: Aprovado

n1 = float(input('Digite a nota1: '))
n2 = float(input('Digite a nota2: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('Você está reprovado.')
elif media < 7.0:
    print('Você está de recuperação.')
else:
    print('Você está aprovado!')


# if 5 < media <= 6.9:
#     print('Você está de recuperação.')
