# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.

s = count = 0
while True:
    numero = int(input('Digite um número inteiro [999 para parar]: '))
    if numero == 999:
        break
    s += numero
    count += 1

print(f'Você digitou {count} números inteiros e o resultado da soma deles foi: {s}')
