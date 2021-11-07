# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1.00 = R$3.27

reais = float(input('Quanto tu tem na carteira? R$'))
print('Você consegue comprar \033[32m${:.2f}\033[m dólares com esse dinheiro'.format(reais/3.27))