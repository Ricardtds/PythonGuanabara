# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada um individualmente.
lista = []
while True:
    nome = str(input('Digite seu nome: '))
    n1 = float(input('Digite a sua primeira nota: '))
    n2 = float(input('Digite a sua segunta nota: '))
    notas = [n1, n2]
    dados = [nome, notas[:]]
    lista.append(dados[:])
    dados.clear()
    notas.clear()
    while True:
        opcao = str(input('Deseja cadastrar mais alguém[S/N]? ')).strip().lower()[0]
        if opcao in 'sn':
            break
    if opcao in 'n':
        break

print('-='*15)
print(f'{"No.":<4}{"NOME":<20}{"MÉDIA"}')
print('-'*30)
for pos, x in enumerate(lista):
    print(f'{pos:<4}{x[0]:<19} {((x[1][0]+x[1][1])/2):.2f}')
print('-'*30)

while True:
    while True:
        aluno = int(input('Deseja mostrar as notas de qual aluno? (999 para parar): '))
        if 0 <= aluno < len(lista) or aluno == 999:
            break
    if aluno == 999:
        break
    else:
        print(f'Notas de {lista[aluno][0]} são {lista[aluno][1][0]} e {lista[aluno][1][1]}')

# lista[ [nome, [n1, n2]], [nome, [n1, n2]] ]
