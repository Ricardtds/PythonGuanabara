# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
# pares. Se for impar vai desconsiderar
s = 0
for x in range(6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        s += numero

print(s)
