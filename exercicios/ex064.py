# Crie um programa que leia vários números inteiros pelo teclado. O programa só
# vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
count = somatorio = 0
numero = int(input('Digite um número diferente de 999: '))
while numero != 999:
    count += 1
    somatorio += numero
    numero = int(input('Digite um número diferente de 999: '))

print('Você digitou {} vezes e o somatório foi de {}'.format(count, somatorio))
