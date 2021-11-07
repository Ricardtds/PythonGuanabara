# Faça um programa que leia um número Inteiro  e mostre na tela o seu sucessor e o seu antecessor
numero = int(input('Digite um numero inteiro: '))
print('Você digitou o numero \033[44m{}\033[m seu antecessor é \033[42m{}\033[m e seu sucessor vale \033[41m{}\033[m '.format(numero, numero-1, numero+1))
