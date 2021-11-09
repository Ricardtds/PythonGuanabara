# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final o programa, mostra:

# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.
idadetotal = 0
homem_velho_nome = ''
homem_velho_idade = 0
qtd_mulheres_jovens = 0
for x in range(4):
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = int(input('Seu sexo? 1 = Masculino, 2 = Feminino: '))
    idadetotal += idade
    if (sexo == 1) and (idade > homem_velho_idade):
        homem_velho_nome = nome
        homem_velho_idade = idade
    if (sexo == 2) and (idade < 20):
        qtd_mulheres_jovens += 1

media_idades = idadetotal / 4

print('A média de idades é: {}'.format(media_idades))
print('O Homem mais velho é: {}'.format(homem_velho_nome))
print('Temos {} mulheres com menos de 20 anos'.format(qtd_mulheres_jovens))
