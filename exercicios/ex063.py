# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os
# n primeiros elementos de uma Sequência de Fibonacci

# EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
c = 2
n1 = 0
n2 = 1

numero = int(input('Número de termos da sequencia fibo: '))
print('{} -> {} ->'.format(n1, n2), end=" ")
while c < numero:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print('{} -> '.format(n3) if c < numero - 1 else '{} -> FIM'.format(n3), end='')
    c += 1
