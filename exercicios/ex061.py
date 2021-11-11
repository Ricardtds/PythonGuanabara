# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos e progressão usando a estrtutura while

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# no final, mostre os 10 primeiros termos dessa progressão.


termo_a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 0
s = termo_a1

while c < 10:
    if c != 9:
        print('{} -> '.format(s), end="")
    else:
        print(s)
    s += razao
    c += 1
