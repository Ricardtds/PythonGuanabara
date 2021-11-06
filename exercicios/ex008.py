# Escreva um programa que leia um valor em metros eo exiba convertido em centimetros e milimetros
metros = float(input('Digite quantos metros deseja: '))
print('Voce digitou {} metros\nEquivale a {:.0f}cm\nEquuivale a {:.0f}mm'.format(metros, metros*100, metros*1000))
