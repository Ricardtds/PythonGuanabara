# Um professor quer sortear um dos seus quartos alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escilhido.
from random import choice

aluno1 = input('Digite o aluno1: ')
aluno2 = input('Digite o aluno2: ')
aluno3 = input('Digite o aluno3: ')
aluno4 = input('Digite o aluno4: ')

listaalunos = [aluno1, aluno2, aluno3, aluno4]

sorteado = choice(listaalunos)

print('O aluno sorteado foi {}'.format(sorteado))
