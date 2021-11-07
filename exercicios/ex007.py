# Desenvolva um programa que leia as duas notas de um aluno, calcula e mostra sua média
nota1 = float(input('Digite a sua nota1: '))
nota2 = float(input('Digite a sua nota2: '))
print('A sua média é: \033[30;41m{}\033[m'.format((nota1+nota2)/2))
