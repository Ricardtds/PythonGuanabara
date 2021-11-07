# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# E R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('Sua passagem custará R$ {:.2f}'.format(preco))