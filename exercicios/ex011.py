# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tintanecessária para pintá-lo, sabendo que cada litro de tinta pinta uma área de 2m

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = altura * largura
tintanecessaria = area / 2
print('A sua parede tem {} metros quadrados\nSerá necessário {} litros de tinta para pintar'.format(area,tintanecessaria))
