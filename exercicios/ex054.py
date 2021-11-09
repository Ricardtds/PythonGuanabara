# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.
# Considere maioridade = 21

from datetime import date

anoprovisorio = 2017

ano_atual = anoprovisorio or date.today().year
qtd_pessoas_jovems = 0
qtd_pessoas_adultas = 0
print(ano_atual)
for x in range(7):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        qtd_pessoas_adultas += 1
    else:
        qtd_pessoas_jovems += 1

print('Temos {} pessoas jovems\nTemos {} pessoas adultas'.format(qtd_pessoas_jovems, qtd_pessoas_adultas))
