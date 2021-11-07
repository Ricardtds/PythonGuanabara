# # O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.
# # Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
# import random
#
# aluno1 = input('Digite o aluno1: ')
# aluno2 = input('Digite o aluno2: ')
# aluno3 = input('Digite o aluno3: ')
# aluno4 = input('Digite o aluno4: ')
# ordem = []
#
# alunos = [aluno1, aluno2, aluno3, aluno4]
#
# sorteado = random.choice(alunos)
# print(sorteado)
# alunos.remove(sorteado)
# ordem.append(sorteado)
#
# sorteado = random.choice(alunos)
# print(sorteado)
# alunos.remove(sorteado)
# ordem.append(sorteado)
#
# sorteado = random.choice(alunos)
# print(sorteado)
# alunos.remove(sorteado)
# ordem.append(sorteado)
#
# sorteado = random.choice(alunos)
# print(sorteado)
# alunos.remove(sorteado)
# ordem.append(sorteado)
#
# print(ordem)

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)

print(random.sample([n1, n2, n3, n4], k=4))
