# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela:

aluno = {
    'Nome': str(input('Qual o nome do aluno: ')),
    'Média': float(input('Qual a média do aluno: '))
}
aluno['Situação'] = 'Aprovado' if aluno['Média'] > 6 else 'Reprovado'
print()
for k, v in aluno.items():
    print(f' {k} é igual a {v}')
