# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final, mostre os 10
# primeiros termos dessa progressão.

termo_1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
s = termo_1
for x in range(1, 11, 1):
    print('{}º termo vale: {}'.format(x, s))
    s += razao
