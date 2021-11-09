# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
# e o menor peso lido.

for x in range(5):
    peso = float(input('Digite teu peso: '))
    if x == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if maior_peso < peso:
            maior_peso = peso
        if menor_peso > peso:
            menor_peso = peso

print('O maior peso foi: {}\nO menor peso foi: {}'.format(maior_peso, menor_peso))
